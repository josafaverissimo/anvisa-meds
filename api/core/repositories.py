import math

import xlrd

from .settings import PMVG_FILE_PATH, PMVG_COLUMNS, MEDS_ITEMS_PER_PAGE
from .models import Substances, Meds, Laboratories, LaboratoriesMeds

from django.db.models import F, Count
from django.db.models.functions import Concat


class MedsPriceRepository:
    COLUMNS_ROW_INDEX = 52
    DATA_ROW_INDEX = 54
    sheet: xlrd.sheet.Sheet

    def __init__(self):
        self.sheet = xlrd.open_workbook(PMVG_FILE_PATH).sheet_by_index(0)

    def get_columns(self) -> dict:
        return self.get_row_data(self.COLUMNS_ROW_INDEX)

    def get_row_data(self, row_index: int) -> dict:
        return {
            col_name: self.sheet.cell_value(rowx=row_index, colx=col_index)
            for col_name, col_index in PMVG_COLUMNS.items()
        }

    def get_rows_data(self):
        return [
            self.get_row_data(row_index)
            for row_index in range(self.DATA_ROW_INDEX, self.sheet.nrows)
        ]


class SubstancesRepository:
    def save(self, name: str):
        substance_stored = Substances.objects.filter(name=name).first()

        if substance_stored is not None:
            return substance_stored.id
        
        substances = Substances(name=name)

        substances.save()

        return substances.id


class MedsRepository:
    def save(
        self,
        substance_id,
        registration,
        fabric_price_no_taxes,
        max_sale_price_government
    ):
        stored_med = Meds.objects.filter(registration=registration).first()

        if stored_med is not None:
            return stored_med.id

        meds = Meds(
            substance_id=substance_id,
            registration=registration,
            fabric_price_no_taxes=fabric_price_no_taxes,
            max_sale_price_government=max_sale_price_government
        )

        meds.save()

        return meds.id


class LaboratoriesRepository:
    def save(self, name: str, cnpj: str) -> int:
        stored_laboratory = Laboratories.objects.filter(cnpj=cnpj).first()

        if stored_laboratory is not None:
            return stored_laboratory.id

        laboratories = Laboratories(name=name, cnpj=cnpj)

        laboratories.save()

        return laboratories.id


class LaboratoriesMedsRepository:
    ITEMS_PER_PAGE = MEDS_ITEMS_PER_PAGE

    def save(self, laboratory_id: int, med_id: int):
        stored_laboratory_med = LaboratoriesMeds.objects.filter(
            laboratory_id=laboratory_id,
            med_id=med_id
        ).first()

        if stored_laboratory_med is not None:
            return stored_laboratory_med.id

        laboratories_meds = LaboratoriesMeds(laboratory_id=laboratory_id, med_id=med_id)

        laboratories_meds.save()

        return laboratories_meds.id

    def get_total_pages(self):
        query = LaboratoriesMeds.objects.select_related('laboratory', 'med__substance') \
          .annotate(concatenated_name=Concat(F('med__substance__name'), F('laboratory__name'))) \
          .aggregate(total_pages=Count('concatenated_name', distinct=True))

        return math.ceil(query['total_pages'] / self.ITEMS_PER_PAGE)

    def get_by_page(self, page: int = 1):
        offset = (page - 1) * self.ITEMS_PER_PAGE
        limit = self.ITEMS_PER_PAGE * page

        query = LaboratoriesMeds.objects.select_related('laboratory', 'med__substance')
        result = query.all().values(
            lab_name=F('laboratory__name'),
            lab_cnpj=F('laboratory__cnpj'),
            substance_name=F('med__substance__name')
        ).distinct()[offset:limit]

        return {
            'total_pages': self.get_total_pages(),
            'data': result
        }
