<script setup lang="ts">
import { computed, reactive } from 'vue'
import { loseLose } from "@/utils/hash";

import Title from '@/components/atomic/atoms/table/Title.vue'
import Input from '@/components/atomic/atoms/Input.vue'
import Button from '@/components/atomic/atoms/button/Button.vue'
import Icon from "@/components/atomic/atoms/Icon.vue";
import Spinner from "@/components/atomic/atoms/Spinner.vue";

interface Filters {
  medSubstance: string
  laboratoryName: string
  laboratoryCnpj: string
  term: string
}

export interface TableMetaData {
  page: number
  filters: Filters
}

const props = withDefaults(defineProps<{
  headers : string[]
  rows : string[][]
  currentPage: number
  totalPages: number
  isLoading?: boolean
}>(), {
  isLoading: false
})

const emits = defineEmits<{
  changePage: [tableMetaData: TableMetaData]
  filter: [tableMetaData: TableMetaData]
}>()

const MAX_ROW_LENGTH = 50

const filters = reactive<Filters>({
  medSubstance: '',
  laboratoryName: '',
  laboratoryCnpj: '',
  term: ''
})

const rowsTitle = reactive<{data: Map<number, string>}>({
  data: new Map()
})

const computedPagesRange = computed(() => {
  const pages = []

  for(let page = 1; page <= props.totalPages; page++) {
    pages.push(page)
  }

  return pages
})

const computedRows = computed(() => props.rows.map(
    cells => cells.map(cell => {
      if(cell.length > MAX_ROW_LENGTH) {
        const newCellValue = `${cell.slice(0, MAX_ROW_LENGTH)}...`
        rowsTitle.data.set(loseLose(newCellValue), cell)

        return newCellValue
      }

      return cell
    })
  )
)

function changePage(pageTarget: number) {
  if(pageTarget < 1 || pageTarget > props.totalPages) {
    return
  }

  emits('changePage', {
    page: pageTarget,
    filters
  })
}

function changeSelectPageHandler(event: Event) {
  changePage(Number(event.target!.value))
}

function filter() {
  emits('filter', {
    page: props.currentPage,
    filters
  })
}

</script>

<template>
  <div class="myTable--wrapper" :class="isLoading ? 'loading': ''">
    <div class="myTable__spinner" v-if="isLoading">
      <Spinner :size="7"/>
    </div>

    <div class="myTable">
      <div class="myTable__header">
        <div class="myTable__header__title">
          <Title>Lista de medicamentos</Title>
        </div>

        <div class="myTable__header__filters">
          <Input
            id="med_substance"
            icon="Substance"
            placeholder="Filtrar por Substância"
            type="search"
            v-model="filters.medSubstance"
          />
          <Input
            id="laboratory_name"
            icon="Laboratory"
            placeholder="Filtrar por Laboratório"
            type="search"
            v-model="filters.laboratoryName"
          />
          <Input
              id="laboratory_cnpj"
              icon="Cnpj"
              placeholder="Filtrar por Cnpj"
              type="search"
              v-model="filters.laboratoryCnpj"
          />
          <Input
              id="full_text_search"
              icon="Search"
              placeholder="Busca Geral"
              type="search"
              v-model="filters.term"
          />
        </div>

        <div class="myTable__header__filterWrapper">
          <Button class="pointer primary filterBtn" @click="filter">Buscar</Button>
        </div>
      </div>

      <div class="myTable__body">
        <table>
          <thead>
            <tr>
              <th v-for="(header, key) in headers" :key="key">{{header}}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(cells, key) in computedRows" :key="key">
              <td
                  v-for="(cell, key) in cells"
                  :key="key"
                  :title="rowsTitle.data.get(loseLose(cell)) ?? cell"
                  :class="rowsTitle.data.get(loseLose(cell)) !== undefined ? 'help' : ''"
              >
                {{cell}}
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="myTable__footer">
        <Button class="pointer" @click="changePage(currentPage - 1)">
          <Icon icon="Previous" :size="2"/>
        </Button>

        Página
        <select class="myTable__footer__currentPage" @change="changeSelectPageHandler($event)">
          <option
              v-for="(page, key) in computedPagesRange"
              :value="page"
              :key="key"
              :selected="page === props.currentPage"
          >
            {{page}}
          </option>
        </select>
        de {{totalPages}}

        <Button class="pointer" @click="changePage(currentPage + 1)">
          <Icon icon="Next" :size="2"/>
        </Button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.loading {
  opacity: .5;
  pointer-events: none;
}

.myTable--wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.myTable__spinner {
  position: absolute;
}

.myTable {
  width: 80%;
  display: flex;
  flex-direction: column;

  .myTable__header {
    padding-bottom: var(--padding-md);

    .myTable__header__title {
      display: flex;
      justify-content: center;
      padding-bottom: var(--padding-md);
    }

    .myTable__header__filters {
      display: flex;
      justify-content: center;
      gap: 2rem;
      padding-bottom: var(--padding-sm);
    }

    .myTable__header__filterWrapper {
      display: flex;
      justify-content: center;

      .filterBtn {
        width: 15%;
        font-size: var(--size-text-md);
      }
    }
  }

  .myTable__body {
    background-color: var(--color-background);
    border: thin solid var(--color-light-shade);
    border-top-left-radius: var(--border-radius-sm);
    border-top-right-radius: var(--border-radius-sm);
    height: 50vh;
    overflow-y: auto;
    box-shadow: var(--shadow-md);

    table {
      width: 100%;

      th,
      td {
        text-align: center;
        padding: var(--padding-sm) 0;

        &.help {
          cursor: help;
        }
      }

      thead {
        position: sticky;
        top: 0;
        background-color: var(--color-background);
        box-shadow: var(--shadow-sm);

        tr {
          th {
            border-bottom: thin solid var(--color-light-shade);
          }
        }
      }

      tbody {
        tr:not(:last-child) {
          border-bottom: thin solid var(--color-light-shade);
        }

        tr:nth-child(2n - 1) {
          background-color: var(--color-background-content);
        }
      }
    }
  }

  .myTable__footer {
    background-color: var(--color-background);
    border-bottom-left-radius: var(--border-radius-sm);
    border-bottom-right-radius: var(--border-radius-sm);

    display: flex;
    justify-content: flex-end;
    align-items: center;

    padding: var(--padding-sm);
    box-shadow: var(--shadow-sm);

    .myTable__footer__currentPage {
      margin: 0 var(--padding-sm);
      padding: var(--padding-sm);
    }
  }
}
</style>
