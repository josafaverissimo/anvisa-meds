from os import getcwd


PMVG_FILE_PATH = f'{getcwd()}/data/pmvg.xls'

LOGGER_FILE_PATH = f'{getcwd()}/core/logs/loguru.log'

PMVG_COLUMNS = {
    'substance': 0,
    'cnpj': 1,
    'laboratory': 2,
    'registration': 4,
    'fabric_price_no_taxes': 13,
    'max_sale_price_government': 34
}

MEDS_ITEMS_PER_PAGE = 25
