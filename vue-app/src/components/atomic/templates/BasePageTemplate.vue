<script setup lang="ts">
import Header from '@/components/atomic/molecules/navigation/Header.vue'

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

    </main>
  </section>
</template>
