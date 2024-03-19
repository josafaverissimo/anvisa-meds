<script setup lang="ts">
import Input from '../Input.vue'

defineProps<{
  id: string
}>()
</script>

<template>
  <Input :id="id" icon="Search" type="search" placeholder="Busca Geral" />
</template>

<style scoped></style>
