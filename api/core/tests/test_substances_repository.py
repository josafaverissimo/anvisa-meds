from django.test import TestCase

from core.repositories import SubstancesRepository


class SubstancesRepositoryTestCase(TestCase):
    def setUp(self):
        self.substances_repository = SubstancesRepository()

    def test_save(self):
        """
        Teste sobre o método save
        """
        substance_id = self.substances_repository.save('PickThisOne')

        self.assertGreater(substance_id, 0, f'Um id deveria ser retornado')


