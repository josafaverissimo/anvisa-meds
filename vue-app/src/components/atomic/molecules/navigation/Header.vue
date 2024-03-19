<script setup lang="ts">
import Title from '@/components/atomic/atoms/navigation/Title.vue'
import ToggleThemeButton from '@/components/atomic/molecules/ToggleThemeButton.vue'
import Logo from '@/components/atomic/atoms/Logo.vue'

defineProps<{
  iconSize: number
}>()
</script>

<template>
  <header class="header">
    <div class="header__titleWrapper">
      <Logo />
      <Title>
        <slot name="title" />
      </Title>
    </div>

    <ToggleThemeButton :iconSize="iconSize" />
  </header>
</template>

<style scoped>
.header {
  padding: var(--padding-sm);
  border: var(--border-thin);
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: var(--color-background);

  .header__titleWrapper {
    display: flex;
    align-items: center;
    gap: var(--padding-sm);
  }
}
</style>
