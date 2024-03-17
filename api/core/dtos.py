from dataclasses import dataclass

from typing import Optional


@dataclass
class LaboratoriesMedsSearchDto:
    med_substance: str = ''
    laboratory_cnpj: str = ''
    laboratory_name: str = ''
    term: str = ''
