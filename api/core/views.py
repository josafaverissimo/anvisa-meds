from rest_framework.views import APIView
from rest_framework.response import Response

from .repositories import \
    MedsPriceRepository, \
    SubstancesRepository, \
    MedsRepository, \
    LaboratoriesRepository, \
    LaboratoriesMedsRepository


class MedsPriceView(APIView):
    def get(self, request):
        meds_price_repository = MedsPriceRepository()
        substances_repository = SubstancesRepository()
        meds_repository = MedsRepository()
        laboratories_repository = LaboratoriesRepository()
        laboratories_meds_repository = LaboratoriesMedsRepository()
        
        meds_price_rows = meds_price_repository.get_rows_data()

        for row in meds_price_rows:
            substance_id = substances_repository.save(row['substance'])
            med_id = meds_repository.save(
                substance_id=substance_id,
                registration=row['registration'],
                fabric_price_no_taxes=row['fabric_price_no_taxes'],
                max_sale_price_government=row['max_sale_price_government']
            )
            laboratory_id = laboratories_repository.save(name=row['laboratory'], cnpj=row['cnpj'])
            laboratory_med_id = laboratories_meds_repository.save(laboratory_id=laboratory_id, med_id=med_id)

        return Response('Stored')
