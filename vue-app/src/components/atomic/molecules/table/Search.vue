<script setup lang="ts">
defineProps<{
  id: string
}>()
</script>

<template>
  <label :for="id">
    <input type="search" :id="id">
  </label>
</template>

<style scoped></style>