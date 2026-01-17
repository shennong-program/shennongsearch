from __future__ import annotations

from typing import Any, Callable, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd

from ..models import (
    NameSearchResponseMedicinalParts,
    NameSearchResponseProcessingMethods,
    NameSearchResponseSpecialDescriptions,
    NameSearchResponseSpeciesOrigins,
    NameType,
)

GetFunc = Callable[[str, Optional[dict[str, Any]]], Any]


def _to_dataframe(
    items: list[Any],
    string_columns: Optional[list[str]] = None,
) -> "pd.DataFrame":
    try:
        import pandas as pd
    except ImportError as exc:
        raise ImportError(
            "pandas is required for all_dataframe; "
            "install via `pip install pandas`."
        ) from exc

    if not items:
        if string_columns:
            return pd.DataFrame({
                col: pd.Series(dtype="string") for col in string_columns
            })
        return pd.DataFrame()

    first = items[0]
    if hasattr(first, "model_dump"):
        rows = [item.model_dump() for item in items]
    else:
        rows = items

    df = pd.DataFrame(rows)
    if string_columns:
        for col in string_columns:
            if col in df.columns:
                df[col] = df[col].astype("string")
    return df


class _BaseNameTypeAPI:
    def __init__(self, get: GetFunc, name_type: NameType) -> None:
        self._get = get
        self._name_type = name_type

    def _search(self, q: str, page: int, limit: int) -> dict[str, Any]:
        return self._get(
            "/api/name/search",
            params={
                "name_type": self._name_type.value,
                "q": q,
                "page": page,
                "limit": limit,
            },
        )

    def _all(self) -> dict[str, Any]:
        return self._get(
            "/api/name/all",
            params={
                "name_type": self._name_type.value,
            },
        )


class MedicinalPartsAPI(_BaseNameTypeAPI):
    def __init__(self, get: GetFunc) -> None:
        super().__init__(get, NameType.MEDICINAL_PARTS)

    def search(
        self,
        q: str = "",
        page: int = 1,
        limit: int = 20,
    ) -> NameSearchResponseMedicinalParts:
        data = self._search(q=q, page=page, limit=limit)
        return NameSearchResponseMedicinalParts(**data)

    def all(self) -> NameSearchResponseMedicinalParts:
        data = self._all()
        return NameSearchResponseMedicinalParts(**data)

    def all_dataframe(self) -> "pd.DataFrame":
        response = self.all()
        columns = ["en", "zh", "explanation"]
        df = _to_dataframe(response.results, string_columns=columns)
        return df.loc[:, columns]


class ProcessingMethodsAPI(_BaseNameTypeAPI):
    def __init__(self, get: GetFunc) -> None:
        super().__init__(get, NameType.PROCESSING_METHODS)

    def search(
        self,
        q: str = "",
        page: int = 1,
        limit: int = 20,
    ) -> NameSearchResponseProcessingMethods:
        data = self._search(q=q, page=page, limit=limit)
        return NameSearchResponseProcessingMethods(**data)

    def all(self) -> NameSearchResponseProcessingMethods:
        data = self._all()
        return NameSearchResponseProcessingMethods(**data)

    def all_dataframe(self) -> "pd.DataFrame":
        response = self.all()
        rows = []
        for item in response.results:
            row = item.model_dump()
            category = row.pop("category", None)
            if isinstance(category, dict):
                row["category_major"] = category.get("major")
                row["category_minor"] = category.get("minor")
            rows.append(row)
        columns = [
            "en",
            "zh",
            "en_full",
            "category_major",
            "category_minor",
            "explanation",
        ]
        df = _to_dataframe(rows, string_columns=columns)
        return df.loc[:, columns]


class SpecialDescriptionsAPI(_BaseNameTypeAPI):
    def __init__(self, get: GetFunc) -> None:
        super().__init__(get, NameType.SPECIAL_DESCRIPTIONS)

    def search(
        self,
        q: str = "",
        page: int = 1,
        limit: int = 20,
    ) -> NameSearchResponseSpecialDescriptions:
        data = self._search(q=q, page=page, limit=limit)
        return NameSearchResponseSpecialDescriptions(**data)

    def all(self) -> NameSearchResponseSpecialDescriptions:
        data = self._all()
        return NameSearchResponseSpecialDescriptions(**data)

    def all_dataframe(self) -> "pd.DataFrame":
        response = self.all()
        columns = ["en", "zh", "explanation"]
        df = _to_dataframe(response.results, string_columns=columns)
        return df.loc[:, columns]


class SpeciesOriginsAPI(_BaseNameTypeAPI):
    def __init__(self, get: GetFunc) -> None:
        super().__init__(get, NameType.SPECIES_ORIGINS)

    def search(
        self,
        q: str = "",
        page: int = 1,
        limit: int = 20,
    ) -> NameSearchResponseSpeciesOrigins:
        data = self._search(q=q, page=page, limit=limit)
        return NameSearchResponseSpeciesOrigins(**data)


class NameAPI:
    def __init__(self, get: GetFunc) -> None:
        self.species_origins = SpeciesOriginsAPI(get)
        self.medicinal_parts = MedicinalPartsAPI(get)
        self.processing_methods = ProcessingMethodsAPI(get)
        self.special_descriptions = SpecialDescriptionsAPI(get)
