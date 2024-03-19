<template>
  <h1 class="title">{{ title }}</h1>
</template>

<script setup lang="ts">
withDefaults(
  defineProps<{
    title: string
    align?: 'left' | 'center' | 'right'
  }>(),
  {
    align: 'left'
  }
)
</script>

<style scoped>
.title {
  font-size: var(--size-text-lg);
  font-family: var(--font-family-title);
  text-align: v-bind(align);
}
</style>
