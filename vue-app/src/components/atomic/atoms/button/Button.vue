<script setup lang="ts">
defineProps<{
  classes?: string
}>()
</script>

<template>
  <button class="btn" :class="classes">
    <slot />
  </button>
</template>

<style scoped>
.btn {
  background: transparent;
  border: none;
  padding: var(--padding-sm);
  border-radius: var(--border-radius-xs);

  &.pointer {
    cursor: pointer;
  }

  &.primary {
    background-color: var(--color-primary);
    color: var(--color-white);
  }
}
</style>
