<template>
  <span class="myTable__title"><slot /></span>
</template>

<style scoped>
.myTable__title {
  font-size: var(--size-text-lg);
  font-family: var(--font-family-title);
  color: var(--color-text-accent);
  text-transform: uppercase;
}
</style>