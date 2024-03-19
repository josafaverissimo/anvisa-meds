from django.test import TestCase

from core.services import PmvgDataService
from core.repositories import MedsPriceRepository, LaboratoriesMedsRepository


class PmvgDataServiceTestCase(TestCase):
    def setUp(self):
        self.pmvg_data_service = PmvgDataService()
        self.meds_prices_rows = MedsPriceRepository().get_rows_data()[:100]

    def test_insert_pmvg_data_in_database_and_check_if_persist(self):
        """
        Teste se o método retorna true e se está salvando os dados no banco de dados
        """
        self.assertTrue(
            self.pmvg_data_service.insert_pmvg_data_in_database(self.meds_prices_rows),
            'O método deve retorna true ao concluir as inserções'
        )

        rows_length = len(LaboratoriesMedsRepository().get_by_page(1)['data'])

        self.assertGreater(rows_length, 0, f'Não houve inserção alguma')