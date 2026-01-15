import os

import pytest

from shennongsearch import ShennongSearchClient
from shennongsearch.models import NameType

BASE_URL = os.getenv("SHENNONGALPHA_BASE_URL", "https://shennongalpha.westlake.edu.cn")

TEST_CASES = [
    (
        "species_origins (en)",
        NameType.SPECIES_ORIGINS,
        "Ephedra sinica",
        {"la": "Ephedra sinica", "zh": "草麻黄"},
    ),
    (
        "species_origins (zh)",
        NameType.SPECIES_ORIGINS,
        "草麻黄",
        {"la": "Ephedra sinica", "zh": "草麻黄"},
    ),
    (
        "medicinal_parts (en)",
        NameType.MEDICINAL_PARTS,
        "stem herbaceous",
        {"en": "stem herbaceous", "zh": "草质茎"},
    ),
    (
        "medicinal_parts (zh)",
        NameType.MEDICINAL_PARTS,
        "草质茎",
        {"en": "stem herbaceous", "zh": "草质茎"},
    ),
    (
        "processing_methods (en)",
        NameType.PROCESSING_METHODS,
        "segmented",
        {"en": "segmented", "zh": "段制"},
    ),
    (
        "processing_methods (zh)",
        NameType.PROCESSING_METHODS,
        "段制",
        {"en": "segmented", "zh": "段制"},
    ),
    (
        "special_descriptions (en)",
        NameType.SPECIAL_DESCRIPTIONS,
        "black",
        {"en": "black", "zh": "黑"},
    ),
    (
        "special_descriptions (zh)",
        NameType.SPECIAL_DESCRIPTIONS,
        "黑",
        {"en": "black", "zh": "黑"},
    ),
]


def _get_field(item, field):
    return getattr(item, field)


@pytest.mark.api
@pytest.mark.parametrize(
    "label,name_type,q,expected", TEST_CASES, ids=[c[0] for c in TEST_CASES]
)
def test_name_search_examples(label, name_type, q, expected):
    with ShennongSearchClient(base_url=BASE_URL, timeout=10.0) as client:
        resp = client.name.search(name_type, q=q, page=1, limit=1)

    assert resp.results, f"{label}: expected non-empty results"
    assert (
        len(resp.results) == 1
    ), f"{label}: expected 1 result, got {len(resp.results)}"

    item = resp.results[0]
    for field, value in expected.items():
        actual = _get_field(item, field)
        assert actual == value, f"{label}: {field} expected {value!r}, got {actual!r}"
