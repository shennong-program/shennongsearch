from .base import ApiModel


class LangValue(ApiModel):
    zh: str
    pinyin: str


class NmmsnNameElement(ApiModel):
    nmm_type: str
    species_origins: list[tuple[str, str]]
    medicinal_parts: list[tuple[str, str]]
    special_descriptions: list[tuple[str, str]]
    processing_methods: list[tuple[str, str]]


class NmmsnProps(ApiModel):
    nmmsn: str
    nmmsn_zh: LangValue
    nmmsn_name_element: NmmsnNameElement
    nmmsn_explanation: str


class NmmgnProps(ApiModel):
    nmmgn: str
    nmmgn_zh: LangValue
    nmmgn_explanation: str


class SnnmmInner(ApiModel):
    nmm_id: str
    nmmsn: NmmsnProps
    nmmgn: NmmgnProps
    standardized_translation: str
    standardized_translation_zh: str


class NmmHierarchy(ApiModel):
    parent_nmm_id: str | None


class SnnmmRecord(ApiModel):
    nmm_id: str
    snnmm: SnnmmInner
    nmm_hierarchy: NmmHierarchy


class SnnmmQueryResponse(ApiModel):
    total: int
    results: list[SnnmmRecord]
