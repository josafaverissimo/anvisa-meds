<script setup lang="ts">
import { toggleTheme } from '@/services/theme'
import Button from '../atoms/button/Button.vue'
import Icon from '@/components/atomic/atoms/Icon.vue'

defineProps({
  iconSize: {
    type: Number,
    default: 1.5
  }
})
</script>

<template>
  <Button class="pointer" @click="toggleTheme">
    <Icon icon="ThemeLightDark" :size="iconSize" />
  </Button>
</template>
