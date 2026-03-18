import pytest
from pydantic import ValidationError

from shennongsearch import SnnmmQueryResponse


def _make_payload():
    return {
        "total": 1,
        "results": [
            {
                "nmm_id": "nmm-0001",
                "snnmm": {
                    "nmm_id": "nmm-0001",
                    "nmmsn": {
                        "nmmsn": "Artemisia annua Part-aerial",
                        "nmmsn_zh": {
                            "zh": "黄花蒿地上部",
                            "pinyin": "huang hua hao di shang bu",
                        },
                        "nmmsn_name_element": {
                            "nmm_type": "plant",
                            "species_origins": [["Artemisia annua", "黄花蒿"]],
                            "medicinal_parts": [["part aerial", "地上部"]],
                            "special_descriptions": [],
                            "processing_methods": [],
                        },
                        "nmmsn_explanation": "Example explanation",
                    },
                    "nmmgn": {
                        "nmmgn": "Qing-hao",
                        "nmmgn_zh": {
                            "zh": "青蒿",
                            "pinyin": "qing hao",
                        },
                        "nmmgn_explanation": "Example generic explanation",
                    },
                },
                "nmm_hierarchy": {
                    "parent_nmm_id": None,
                },
            }
        ],
    }


def test_snnmm_query_response_accepts_standardized_translation_fields():
    payload = _make_payload()
    payload["results"][0]["snnmm"]["standardized_translation"] = (
        "Artemisia annua Part-aerial (NMM-0001, Qing-hao)"
    )
    payload["results"][0]["snnmm"]["standardized_translation_zh"] = (
        "黄花蒿地上部（NMM-0001，青蒿）"
    )

    resp = SnnmmQueryResponse(**payload)

    item = resp.results[0]
    assert (
        item.snnmm.standardized_translation
        == "Artemisia annua Part-aerial (NMM-0001, Qing-hao)"
    )
    assert item.snnmm.standardized_translation_zh == "黄花蒿地上部（NMM-0001，青蒿）"


def test_snnmm_query_response_requires_standardized_translation_fields():
    with pytest.raises(ValidationError):
        SnnmmQueryResponse(**_make_payload())
