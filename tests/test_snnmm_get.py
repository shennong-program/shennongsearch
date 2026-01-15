import os

import pytest

from shennongsearch import ShennongSearchClient

BASE_URL = os.getenv("SHENNONGALPHA_BASE_URL", "https://shennongalpha.westlake.edu.cn")


TEST_CASES = [
    ("nmm_id", {"nmm_id": "nmm-0001"}),
    ("nmmsn", {"nmmsn": "Artemisia annua Part-aerial"}),
    ("nmmsn_zh", {"nmmsn_zh": "黄花蒿地上部"}),
    ("nmmgn", {"nmmgn": "Qing-hao"}),
    ("nmmgn_zh", {"nmmgn_zh": "青蒿"}),
]

EXPECTED = {
    "nmm_id": "nmm-0001",
    "nmmsn": "Artemisia annua Part-aerial",
    "nmmsn_zh": "黄花蒿地上部",
    "nmmgn": "Qing-hao",
    "nmmgn_zh": "青蒿",
}


@pytest.mark.api
@pytest.mark.parametrize("label,params", TEST_CASES, ids=[c[0] for c in TEST_CASES])
def test_snnmm_query_by_field(label, params):
    with ShennongSearchClient(base_url=BASE_URL, timeout=10.0) as client:
        resp = client.snnmm.get(**params)

    assert resp.results, f"{label}: expected non-empty results"
    assert resp.total == 1, f"{label}: expected total=1, got {resp.total}"
    assert (
        len(resp.results) == 1
    ), f"{label}: expected 1 result, got {len(resp.results)}"

    item = resp.results[0]
    assert item.nmm_id == EXPECTED["nmm_id"]
    assert item.snnmm.nmm_id == EXPECTED["nmm_id"]
    assert item.snnmm.nmmsn.nmmsn == EXPECTED["nmmsn"]
    assert item.snnmm.nmmsn.nmmsn_zh.zh == EXPECTED["nmmsn_zh"]
    assert item.snnmm.nmmgn.nmmgn == EXPECTED["nmmgn"]
    assert item.snnmm.nmmgn.nmmgn_zh.zh == EXPECTED["nmmgn_zh"]
