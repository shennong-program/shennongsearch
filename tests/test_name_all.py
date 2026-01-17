import os

import pytest

from shennongsearch import ShennongSearchClient
BASE_URL = os.getenv("SHENNONGALPHA_BASE_URL", "https://shennongalpha.westlake.edu.cn")

TEST_CASES = [
    ("medicinal_parts", "medicinal_parts", 300),
    ("processing_methods", "processing_methods", 50),
    ("special_descriptions", "special_descriptions", 20),
]


@pytest.mark.api
@pytest.mark.parametrize(
    "label,api_name,min_total", TEST_CASES, ids=[c[0] for c in TEST_CASES]
)
def test_name_all_min_counts(label, api_name, min_total):
    with ShennongSearchClient(base_url=BASE_URL, timeout=20.0) as client:
        api = getattr(client.name, api_name)
        resp = api.all()

    assert (
        resp.total >= min_total
    ), f"{label}: expected total >= {min_total}, got {resp.total}"
    assert (
        len(resp.results) >= min_total
    ), f"{label}: expected results >= {min_total}, got {len(resp.results)}"
