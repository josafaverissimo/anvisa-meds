<script setup lang="ts">
import { computed, defineAsyncComponent } from 'vue'

interface IconStyles {
  height: string
  fill?: string
}

const props = withDefaults(
  defineProps<{
    icon: string
    size?: number
    color?: string
  }>(),
  {
    size: 1,
    color: 'text'
  }
)

const iconComponent = computed(() =>
  defineAsyncComponent(() => import(`../../icons/${props.icon}Icon.vue`))
)

const iconStyles: IconStyles = {
  height: `${props.size}rem`
}

if (props.color) {
  iconStyles['fill'] = `var(--color-${props.color})`
}
</script>

<template>
  <component :is="iconComponent" :style="iconStyles" />
</template>
