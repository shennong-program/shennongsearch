from __future__ import annotations

from typing import Any, Callable, Optional

from ..models import (
    NameSearchResponseMedicinalParts,
    NameSearchResponseProcessingMethods,
    NameSearchResponseSpecialDescriptions,
    NameSearchResponseSpeciesOrigins,
    NameType,
)

GetFunc = Callable[[str, Optional[dict[str, Any]]], Any]
NameSearchResponse = (
    NameSearchResponseSpeciesOrigins
    | NameSearchResponseMedicinalParts
    | NameSearchResponseProcessingMethods
    | NameSearchResponseSpecialDescriptions
)


class NameAPI:
    def __init__(self, get: GetFunc) -> None:
        self._get = get

    def search(
        self,
        name_type: NameType | str,
        q: str = "",
        page: int = 1,
        limit: int = 20,
    ) -> NameSearchResponse:
        if isinstance(name_type, NameType):
            name_type_value = name_type.value
        else:
            name_type_value = NameType(name_type).value

        data = self._get(
            "/api/name/search",
            params={
                "name_type": name_type_value,
                "q": q,
                "page": page,
                "limit": limit,
            },
        )

        if name_type_value == NameType.SPECIES_ORIGINS.value:
            return NameSearchResponseSpeciesOrigins(**data)
        if name_type_value == NameType.MEDICINAL_PARTS.value:
            return NameSearchResponseMedicinalParts(**data)
        if name_type_value == NameType.PROCESSING_METHODS.value:
            return NameSearchResponseProcessingMethods(**data)
        if name_type_value == NameType.SPECIAL_DESCRIPTIONS.value:
            return NameSearchResponseSpecialDescriptions(**data)

        raise ValueError(f"Unsupported name_type: {name_type_value}")
