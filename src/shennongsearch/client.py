from __future__ import annotations

from typing import Any, Optional

import httpx

from .api import NameAPI, SnnmmAPI
from .exceptions import ShennongSearchError

DEFAULT_BASE_URL = "https://shennongalpha.westlake.edu.cn"


class ShennongSearchClient:
    def __init__(self, base_url: str = DEFAULT_BASE_URL, timeout: float = 10.0):
        self._client = httpx.Client(base_url=base_url, timeout=timeout)
        self.name: NameAPI = NameAPI(self._get)
        self.snnmm: SnnmmAPI = SnnmmAPI(self._get)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "ShennongSearchClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def _handle_response(self, response: httpx.Response) -> Any:
        if response.is_error:
            message = response.reason_phrase
            user_message = None
            try:
                payload = response.json()
            except ValueError:
                payload = None

            if isinstance(payload, dict):
                message = payload.get("message", message)
                user_message = payload.get("user_message")

            raise ShennongSearchError(
                message=message,
                status_code=response.status_code,
                user_message=user_message,
            )

        try:
            return response.json()
        except ValueError as exc:
            raise ShennongSearchError("Invalid JSON response") from exc

    def _get(self, path: str, params: Optional[dict[str, Any]] = None) -> Any:
        try:
            response = self._client.get(path, params=params)
        except httpx.RequestError as exc:
            raise ShennongSearchError(str(exc)) from exc
        return self._handle_response(response)
