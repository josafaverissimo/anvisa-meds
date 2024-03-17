<script setup lang="ts">
import Title from '@/components/atomic/atoms/navigation/Title.vue'
import ToggleThemeButton from '@/components/atomic/molecules/ToggleThemeButton.vue'

defineProps<{
  iconSize: number
}>()
</script>

<template>
  <header class="header">
    <div class="header__titleWrapper">
      <img src="/logo.png" alt="">
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
  border-bottom: 1px solid var(--color-light-shade);
  display: flex;
  justify-content: space-between;
  align-items: center;

  .header__titleWrapper {
    display: flex;
    align-items: center;
    gap: var(--padding-sm);

    img {
      width: 3rem;
      height: 3rem;
      object-fit: contain;
    }
  }
}
</style>
