from __future__ import annotations

from typing import Any, Callable, Optional

from ..models import SnnmmQueryResponse

GetFunc = Callable[[str, Optional[dict[str, Any]]], Any]


class SnnmmAPI:
    def __init__(self, get: GetFunc) -> None:
        self._get = get

    def get(
        self,
        *,
        nmm_id: Optional[str] = None,
        nmmsn: Optional[str] = None,
        nmmsn_zh: Optional[str] = None,
        nmmgn: Optional[str] = None,
        nmmgn_zh: Optional[str] = None,
    ) -> SnnmmQueryResponse:
        params: dict[str, str] = {}
        if nmm_id:
            params["nmm_id"] = nmm_id
        if nmmsn:
            params["nmmsn"] = nmmsn
        if nmmsn_zh:
            params["nmmsn_zh"] = nmmsn_zh
        if nmmgn:
            params["nmmgn"] = nmmgn
        if nmmgn_zh:
            params["nmmgn_zh"] = nmmgn_zh

        if len(params) != 1:
            raise ValueError("Provide exactly one query parameter")

        data = self._get("/api/snnmm", params=params)
        return SnnmmQueryResponse(**data)

    def get_by_nmm_id(self, nmm_id: str) -> SnnmmQueryResponse:
        return self.get(nmm_id=nmm_id)

    def get_by_nmmsn_zh(self, nmmsn_zh: str) -> SnnmmQueryResponse:
        return self.get(nmmsn_zh=nmmsn_zh)

    def get_by_nmmgn(self, nmmgn: str) -> SnnmmQueryResponse:
        return self.get(nmmgn=nmmgn)

    def get_by_nmmgn_zh(self, nmmgn_zh: str) -> SnnmmQueryResponse:
        return self.get(nmmgn_zh=nmmgn_zh)
