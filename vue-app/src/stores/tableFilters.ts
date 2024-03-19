import { reactive, watch } from 'vue'
import { defineStore } from "pinia";


export interface Filters {
    medSubstance: string
    laboratoryName: string
    laboratoryCnpj: string
    term: string
}

export const useTableFiltersStore = defineStore('tableFilter', () => {
    const filters = reactive<Filters>({
        medSubstance: localStorage.getItem('medSubstance') ?? '',
        laboratoryName: localStorage.getItem('laboratoryName') ?? '',
        laboratoryCnpj: localStorage.getItem('laboratoryCnpj') ?? '',
        term: localStorage.getItem('term') ?? ''
    })

    watch(filters, (filters: Filters) => {
        for(let key in filters) {
            localStorage.setItem(key, filters[key as keyof Filters])
        }
    })

    return { filters }
})