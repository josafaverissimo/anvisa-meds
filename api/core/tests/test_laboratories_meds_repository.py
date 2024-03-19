from django.test import TestCase

from core.services import PmvgDataService
from core.repositories import \
    LaboratoriesMedsRepository, \
    LaboratoriesRepository, \
    MedsRepository, \
    SubstancesRepository, \
    MedsPriceRepository


class LaboratoriesMedsRepositoryTestCase(TestCase):
    def setUp(self):
        self.laboratories_meds_repository = LaboratoriesMedsRepository()
        self.laboratory_id = LaboratoriesRepository().save('mcz labs', '1231')
        self.substance_id = SubstancesRepository().save('substancia')
        self.med_id = MedsRepository().save(self.substance_id, 12312321, 50, 50)
        self.meds_price_rows = MedsPriceRepository().get_rows_data()[:50]
        self.pmvg_data_service = PmvgDataService()
        self.pmvg_data_service.insert_pmvg_data_in_database(self.meds_price_rows)

    def test_save(self):
        """
        Teste sobre o método save
        """
        laboratory_med_id = self.laboratories_meds_repository.save(self.laboratory_id, self.med_id)

        self.assertGreater(laboratory_med_id, 0, f'Um id deveria ser retornado')

    def test_get_page_returns(self):
        """
        Teste sobre o returno do método
        """
        page = self.laboratories_meds_repository.get_by_page(1)

        self.assertTrue(isinstance(page['total_pages'], int), f'total_pages não é um inteiro')
        self.assertTrue(isinstance(page['data'], list), f'data não é uma lista')
