<script setup lang="ts">

withDefaults(defineProps<{
  classes?: string
  type ?: "button" | "submit" | "reset"
}>(), {
  type: 'button'
})
</script>

<template>
  <button class="btn" :class="classes" :type="type">
    <slot class="content"/>
  </button>
</template>

<style scoped>
.btn {
  background: transparent;
  border: none;
  padding: var(--padding-sm);
  border-radius: var(--border-radius-lg);

  &.pointer {
    cursor: pointer;
  }

  &.circle {
    border-radius: var(--border-radius-circle);
  }

  &.light {
    background-color: var(--color-background-content);
  }

  &.bordered {
    border: var(--border-thin);
  }

  &.primary {
    color: var(--color-primary);
    transition: all .3s;
    border: var(--border-thin);

    &:hover {
      border: thin solid var(--color-primary);
      background-color: var(--color-background);
    }
  }

  &.danger {
    color: var(--color-danger);
    transition: all .3s;
    border: var(--border-thin);

    &:hover {
      border: thin solid var(--color-danger);
      background-color: var(--color-background);
    }
  }
}

.content svg {
  fill: var(--color-white);
}
</style>
