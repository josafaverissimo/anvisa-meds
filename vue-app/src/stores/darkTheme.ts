import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useThemeStore = defineStore('darkTheme', () => {
  const rootElement = document.documentElement
  const currentTheme = ref(localStorage.getItem('theme') ?? rootElement.dataset.theme)

  const setTheme = (theme: string) => {
    localStorage.setItem('theme', theme)
    currentTheme.value = theme
    rootElement.dataset.theme = theme
  }

  return { currentTheme, setTheme }
})
