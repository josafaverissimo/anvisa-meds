from django.db import transaction
from django.db.utils import DatabaseError

from .settings import LOGGER_FILE_PATH

from loguru import logger

from .repositories import \
    MedsPriceRepository, \
    SubstancesRepository, \
    MedsRepository, \
    LaboratoriesRepository, \
    LaboratoriesMedsRepository


logger.add(LOGGER_FILE_PATH)

class PmvgDataService:
    def insert_pmvg_data_in_database(self) -> bool:
        meds_price_repository = MedsPriceRepository()
        substances_repository = SubstancesRepository()
        meds_repository = MedsRepository()
        laboratories_repository = LaboratoriesRepository()
        laboratories_meds_repository = LaboratoriesMedsRepository()

        meds_price_rows = meds_price_repository.get_rows_data()

        for row in meds_price_rows:
            try:
                with transaction.atomic():
                    substance_id = substances_repository.save(row['substance'])
                    med_id = meds_repository.save(
                        substance_id=substance_id,
                        registration=row['registration'],
                        fabric_price_no_taxes=row['fabric_price_no_taxes'],
                        max_sale_price_government=row['max_sale_price_government']
                    )
                    laboratory_id = laboratories_repository.save(name=row['laboratory'], cnpj=row['cnpj'])
                    laboratories_meds_repository.save(laboratory_id=laboratory_id, med_id=med_id)
            except DatabaseError as error:
                logger.error(f'{error}\n{row}')
                return False

        return True
