<script setup lang="ts">
import Header from '@/components/atomic/molecules/navigation/Header.vue'
import Table from '@/components/atomic/organisms/table/Table.vue'

defineProps<{
  iconSize: number
}>()
</script>

<template>
  <section class="mainSection">
    <Header :iconSize="iconSize">
      <template #title>
        <slot name="headerTitle" />
      </template>
    </Header>

    <main class="mainContent">
      <Table />
    </main>
  </section>
</template>

<style scoped>
.mainContent {
  padding: var(--padding-md);
}
</style>
