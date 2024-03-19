<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(
  defineProps<{
    message: string
    status?: string
    color?: string
  }>(),
  {
    status: 'background',
    color: 'text'
  }
)

const statusComputed = computed(() => `var(--color-${props.status})`)
const colorComputed = computed(() => `var(--color-${props.color})`)
</script>

<template>
  <div class="toast">
    <span class="toast__message">{{ message }}</span>
  </div>
</template>

<style scoped>
.toast {
  background-color: v-bind(statusComputed);
  border: var(--border);
  color: v-bind(colorComputed);
  border-radius: var(--border-radius-xs);
  padding: var(--padding-sm);

  .toast__message {
    font-size: var(--size-text-sm);
  }

  svg {
    fill: v-bind(colorComputed);
  }
}
</style>
