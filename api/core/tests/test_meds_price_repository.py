from django.test import TestCase

from core.repositories import MedsPriceRepository
from core.settings import PMVG_COLUMNS


class MedsPriceRepositoryTestCase(TestCase):
    def setUp(self):
        self.meds_price_repository = MedsPriceRepository()
        self.EXPECTED_COLUMNS_IN_XLS = [
            'substância',
            'cnpj',
            'laboratório',
            'registro',
            'pf sem impostos',
            'pmvg sem imposto'
        ]

    def test_get_columns_keys(self):
        """
        Teste para saber se get_columns retorna as colunas configuradas para retornas em PMVG_COLUMNS
        """
        columns = self.meds_price_repository.get_columns().keys()

        self.assertTrue(len(columns) > 0, f'As colunas estão vazias')

        for column in columns:
            self.assertTrue(column in PMVG_COLUMNS.keys(), f'A coluna {column} não é permitida')

    def test_get_columns_values(self):
        """
        Teste para saber se os valores das colunas do arquivo xls são os esperados
        """
        columns = self.meds_price_repository.get_columns().values()

        for column in columns:
            self.assertTrue(column in self.EXPECTED_COLUMNS_IN_XLS)

    def test_get_row_data_valid_index(self):
        """
        Teste para saber se o retorno do método row_data está correto baseado no índice em um
        intervalo válido: MedsPriceRepository.COLUMNS_ROW_INDEX <= index < self.meds_price_repository.sheet.nrows
        """
        row_data = self.meds_price_repository.get_row_data(MedsPriceRepository.COLUMNS_ROW_INDEX)

        for key, value in row_data.items():
            self.assertTrue(key in PMVG_COLUMNS.keys(), f'A coluna {key} não é permitida')
            self.assertTrue(isinstance(value, str), f'O valor {value} não é uma string')

    def test_get_row_data_invalid_index(self):
        """
        Teste para saber se o retorno do método row_data está correto baseado no índice em um
        intervalo inválido: MedsPriceRepository.COLUMNS_ROW_INDEX >= index >= self.meds_price_repository.sheet.nrows
        """
        row_data = self.meds_price_repository.get_row_data(0)

        self.assertTrue(len(row_data.keys()) == 0, f'O índice não é válido, o retorno deve ser vazio')

    def test_get_row_data_edge_indexes(self):
        """
        Teste para saber se o retorno do método row_data está correto baseado nos índice das extremidades do
        intervalo: MedsPriceRepository.COLUMNS_ROW_INDEX <= index < self.meds_price_repository.sheet.nrows - 1
        """
        row_data = self.meds_price_repository.get_row_data(MedsPriceRepository.COLUMNS_ROW_INDEX)
        self.assertTrue(len(row_data.keys()) > 0, f'O índice é válido, o retorno não deve ser vazio')

        row_data = self.meds_price_repository.get_row_data(self.meds_price_repository.sheet.nrows - 1)
        self.assertTrue(len(row_data.keys()) > 0, f'O índice é válido, o retorno não deve ser vazio')

        row_data = self.meds_price_repository.get_row_data(MedsPriceRepository.COLUMNS_ROW_INDEX - 1)
        self.assertFalse(len(row_data.keys()) > 0, f'O índice não é válido, o retorno deve ser vazio')

        row_data = self.meds_price_repository.get_row_data(self.meds_price_repository.sheet.nrows)
        self.assertFalse(len(row_data.keys()) > 0, f'O índice não é válido, o retorno deve ser vazio')

    def test_get_rows_data_length(self):
        rows_data = self.meds_price_repository.get_rows_data()
        expected_length = self.meds_price_repository.sheet.nrows - MedsPriceRepository.DATA_ROW_INDEX

        self.assertEqual(
            len(rows_data),
            expected_length,
            f'O tamanho não deveria ser {len(rows_data)}, mas sim: {expected_length}'
        )
