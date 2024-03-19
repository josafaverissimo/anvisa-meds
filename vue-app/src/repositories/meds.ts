import { api } from '@/utils/api'

export interface MedRow {
    laboratory_name: string
    laboratory_cnpj: string
    med_substance: string
}

export interface MedDataResponse {
    total_pages: number
    data: MedRow[]
}

export interface Search {
    med_substance?: string
    laboratory_name?: string
    laboratory_cnpj?: string
    term?: string
}

function isSearchValueValid(searchValue?: string) {
    return searchValue !== undefined && searchValue !== ''
}

export class MedsRepository {
    getData(page: number, search: Search) {
        const queryString = new URLSearchParams()

        queryString.append('page', String(page))

        for(let key in search) {
            const searchValue = search[key as keyof Search]

            if(isSearchValueValid(searchValue)) {
                queryString.append(key, searchValue!)
            }
        }

        return api.get<MedDataResponse>(`meds?${queryString.toString()}`).then(response => {
            if(response.data) {
                return response.data
            }

            return {
                total_pages: 0,
                data: []
            }
        })
    }
}