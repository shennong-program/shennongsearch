from __future__ import annotations

from enum import Enum


from .base import ApiModel


class NameType(str, Enum):
    SPECIES_ORIGINS = "species_origins"
    MEDICINAL_PARTS = "medicinal_parts"
    PROCESSING_METHODS = "processing_methods"
    SPECIAL_DESCRIPTIONS = "special_descriptions"


class SpeciesOriginItem(ApiModel):
    la: str
    zh: str
    std: bool


class MedicinalPartItem(ApiModel):
    en: str
    zh: str
    explanation: str


class ProcessingCategory(ApiModel):
    major: str
    minor: str


class ProcessingMethodItem(ApiModel):
    en: str
    zh: str
    en_full: str
    category: ProcessingCategory
    explanation: str


class SpecialDescriptionItem(ApiModel):
    en: str
    zh: str
    explanation: str


class NameSearchResponseSpeciesOrigins(ApiModel):
    q: str
    page: int
    limit: int
    total: int
    results: list[SpeciesOriginItem]


class NameSearchResponseMedicinalParts(ApiModel):
    q: str
    page: int
    limit: int
    total: int
    results: list[MedicinalPartItem]


class NameSearchResponseProcessingMethods(ApiModel):
    q: str
    page: int
    limit: int
    total: int
    results: list[ProcessingMethodItem]


class NameSearchResponseSpecialDescriptions(ApiModel):
    q: str
    page: int
    limit: int
    total: int
    results: list[SpecialDescriptionItem]
