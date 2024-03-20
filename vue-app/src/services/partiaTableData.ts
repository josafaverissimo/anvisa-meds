export interface PartialTableData {
    currentPage: number
}

export const usePartialTableDataService = () => {
    function getStoredPartialTableData(): PartialTableData {
        const storedPartialTableData = localStorage.getItem('partialTableData')

        return storedPartialTableData ? JSON.parse(storedPartialTableData) : {
            currentPage: 1
        }
    }

    function storePartialTableData(partialTableData: PartialTableData) {
        localStorage.setItem('partialTableData', JSON.stringify(partialTableData))
    }

    return { getStoredPartialTableData, storePartialTableData }
}