import { useThemeStore } from '@/stores/darkTheme'

export function toggleTheme() {
  const themeStore = useThemeStore()
  const themeToggled = themeStore.currentTheme === 'light' ? 'dark' : 'light'

  themeStore.setTheme(themeToggled)
}

export function setCurrentTheme() {
  const themeStore = useThemeStore()

  document.documentElement.dataset.theme = themeStore.currentTheme
}
