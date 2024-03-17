<script setup lang="ts">
import { reactive, computed } from 'vue'
import Toast from './Toast.vue'

interface ToastHashMap {
  [key: string]: ToastItem
}

interface ToastItem {
  id?: string
  message: string
  status?: string
  color?: string
}

const toasts = reactive<{ items: ToastHashMap }>({
  items: {}
})

const toastItems = computed(() => Object.values(toasts.items).reverse())

const push = (toastItem: ToastItem, timeToLive = 2250) => {
  const toastId = window.crypto.randomUUID()
  toastItem.id = toastId
  toasts.items[toastId] = toastItem

  setTimeout(() => {
    delete toasts.items[toastId]
  }, timeToLive)
}

defineExpose({ push })
</script>

<template>
  <div class="toastContainer">
    <Toast
      v-for="toast in toastItems"
      :key="toast.id"
      :message="toast.message"
      :status="toast.status"
      :color="toast.color"
    />
  </div>
</template>

<style scoped>
.toastContainer {
  position: absolute;
  top: 0;
  right: 0;
  width: var(--size-toast);
}
</style>
