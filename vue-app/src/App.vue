<script setup lang="ts">
import BasePage from './components/atomic/pages/BasePage.vue'
import { useThemeStore } from "@/stores/darkTheme";

const themeStore = useThemeStore()

themeStore.setTheme(themeStore.currentTheme!)

</script>

<template>
  <BasePage />
</template>

<style scoped></style>
