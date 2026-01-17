import os

import pandas as pd
import pytest

from shennongsearch import ShennongSearchClient

BASE_URL = os.getenv("SHENNONGALPHA_BASE_URL", "https://shennongalpha.westlake.edu.cn")

COLUMN_SPECS = [
    (
        "medicinal_parts",
        ["en", "zh", "explanation"],
    ),
    (
        "special_descriptions",
        ["en", "zh", "explanation"],
    ),
    (
        "processing_methods",
        ["en", "zh", "en_full", "category_major", "category_minor", "explanation"],
    ),
]


def _assert_string_not_null(series, label, column):
    is_string = pd.api.types.is_string_dtype(series) and str(series.dtype) != "object"
    assert is_string, f"{label}: {column} expected pandas string dtype"
    assert not series.isna().any(), f"{label}: {column} has null values"


@pytest.mark.api
@pytest.mark.parametrize(
    "api_name,required_cols",
    COLUMN_SPECS,
    ids=[c[0] for c in COLUMN_SPECS],
)
def test_name_dataframe_columns(api_name, required_cols):
    with ShennongSearchClient(base_url=BASE_URL, timeout=20.0) as client:
        api = getattr(client.name, api_name)
        df = api.all_dataframe()

    assert not df.empty, f"{api_name}: expected non-empty dataframe"

    assert list(df.columns) == required_cols, (
        f"{api_name}: expected columns {required_cols}, got {list(df.columns)}"
    )

    for column in required_cols:
        _assert_string_not_null(df[column], api_name, column)
