from django.test import TestCase

from core.repositories import SubstancesRepository
from core.repositories import MedsRepository


class MedsRepositoryTestCase(TestCase):
    def setUp(self):
        self.meds_repository = MedsRepository()
        self.substance_id = SubstancesRepository().save('TestMe')

    def test_save_valid_types(self):
        """
        Teste sobre o método save
        """
        med_id = self.meds_repository.save(
            substance_id=self.substance_id,
            registration=123,
            fabric_price_no_taxes=10.3,
            max_sale_price_government=20.3
        )

        self.assertGreater(med_id, 0, f'Um id deveria ser retornado')

    def test_save_prices_int(self):
        """
        Teste sobre o método save com os valores para os preços como inteiros
        """
        med_id = self.meds_repository.save(
            substance_id=self.substance_id,
            registration=123,
            fabric_price_no_taxes=10,
            max_sale_price_government=20
        )

        self.assertGreater(med_id, 0, f'Um id deveria ser retornado')
