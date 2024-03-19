<script setup lang="ts">
import Icon from '@/components/atomic/atoms/Icon.vue'

withDefaults(
  defineProps<{
    id: string
    icon?: string
    type?: string
    placeholder?: string
    value ?: string
  }>(),
  {
    type: 'text',
    placeholder: '',
    value: ''
  }
)

const model = defineModel()
</script>

<template>
  <label :for="id" class="inputWrapper">
    <Icon :icon="icon" :size="2" v-if="icon" />
    <input :type="type" :id="id" :placeholder="placeholder" v-model="model"/>
  </label>
</template>

<style scoped>
.inputWrapper {
  display: flex;
  align-items: center;
  padding: var(--padding-sm);
  background-color: var(--color-background);
  border-radius: var(--border-radius-sm);
  transition: all 0.5s;
  border: thin solid var(--color-light-shade);

  &:focus-within {
    box-shadow: var(--shadow-md);
  }

  input {
    background-color: transparent;
    border: none;
    padding: var(--padding-sm);
    outline: none;
    font-size: 1rem;
    color: var(--color-text);
    width: 100%;
    white-space: nowrap;
    text-overflow: ellipsis;
  }
}
</style>
