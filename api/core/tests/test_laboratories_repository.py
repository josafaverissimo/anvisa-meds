from django.test import TestCase

from core.repositories import LaboratoriesRepository


class LaboratoriesRepositoryTestCase(TestCase):
    def setUp(self):
        self.laboratories_repository = LaboratoriesRepository()

    def test_save(self):
        """
        Teste sobre o método save
        """
        laboratory_id = self.laboratories_repository.save('ProMax Labs', '40.028.922/4002-89')

        self.assertGreater(laboratory_id, 0, f'Um id deveria ser retornado')
