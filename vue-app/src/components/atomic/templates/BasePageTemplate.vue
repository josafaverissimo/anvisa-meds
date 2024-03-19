<script setup lang="ts">
import type { MedRow } from '@/repositories/meds';
import { MedsRepository} from "@/repositories/meds";
import {reactive, ref, onMounted, computed} from "vue";
import Header from '@/components/atomic/molecules/navigation/Header.vue'
import type { TableMetaData } from "@/components/atomic/organisms/table/Table.vue";
import Table from '@/components/atomic/organisms/table/Table.vue'
import ToastContainer from '@/components/atomic/molecules/ToastContainer.vue'

defineProps<{
  iconSize: number
}>()

interface TableData {
  headers: string[]
  rows: MedRow[],
  currentPage: number,
  totalPages: number
}

const FIRST_PAGE = 1

const medsRepository = new MedsRepository()

const toastContainer = ref<InstanceType<typeof ToastContainer> | null>(null)

const tableData = reactive<TableData>({
  headers: ['Substância', 'Laboratório', 'Cnpj'],
  rows: [],
  currentPage: 0,
  totalPages: 0
})

const isTableLoading = ref(false)

const computedTableRows = computed((): string[][] => tableData.rows.map(row => [
    row.med_substance,
    row.laboratory_name,
    row.laboratory_cnpj
]))

async function setTableData(tableMetaData: TableMetaData) {
  isTableLoading.value = true

  try {
    const response = (await medsRepository.getData(tableMetaData.page, {
      med_substance: tableMetaData.filters.medSubstance,
      laboratory_name: tableMetaData.filters.laboratoryName,
      laboratory_cnpj: tableMetaData.filters.laboratoryCnpj,
      term: tableMetaData.filters.term
    }))

    if(response) {
      tableData.currentPage = tableMetaData.page
      tableData.totalPages = response.total_pages
      tableData.rows = response.data
    }
  } catch(error) {
    toastContainer.value!.push({
      'message': 'Tivemos um erro interno, tenta mais tarde',
      'status': 'danger',
      'color': 'white'
    })
  } finally {
    isTableLoading.value = false
  }
}

function filterHandler(tableMetaData: TableMetaData) {
  tableMetaData.page = FIRST_PAGE
  setTableData(tableMetaData)
}

onMounted(() => {
  setTableData({
    page: FIRST_PAGE,
    filters: {
      medSubstance: '',
      laboratoryName: '',
      laboratoryCnpj: '',
      term: ''
    }
  })
})
</script>

<template>
  <section class="mainSection">
    <Header :iconSize="iconSize">
      <template #title>
        <slot name="headerTitle" />
      </template>
    </Header>

    <main class="mainContent">
      <ToastContainer ref="toastContainer"/>

      <Table
          :headers="tableData.headers"
          :rows="computedTableRows"
          :currentPage="tableData.currentPage"
          :totalPages="tableData.totalPages"
          @changePage="setTableData"
          @filter="filterHandler"
          :isLoading="isTableLoading"
      />
    </main>
  </section>
</template>

<style scoped>
.mainContent {
  position: relative;
  padding: var(--padding-md);
}
</style>
