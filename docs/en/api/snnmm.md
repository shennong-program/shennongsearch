---
title: SNNMM Query API
---

# SNNMM Query API

Base URL: `https://shennongalpha.westlake.edu.cn`

## GET /api/snnmm

Query SNNMM by system name, common name, or ID. Provide exactly one query parameter per request.

### Query Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `nmm_id` | No | NMM ID, e.g. `nmm-0a1b` |
| `nmmsn` | No | System name (English) |
| `nmmsn_zh` | No | System name (Chinese) |
| `nmmgn` | No | Common name (English) |
| `nmmgn_zh` | No | Common name (Chinese) |

Exactly one of the above parameters must be provided; otherwise the API returns 400.

### Response

```json
{
  "total": 0,
  "results": []
}
```

Each entry in `results` includes fields such as `snnmm`, `nmm_hierarchy`, and `synonyms`. Under `snnmm`, there are also two computed fields: `standardized_translation` and `standardized_translation_zh`.

### Python Usage

```python
from shennongsearch import ShennongSearchClient

client = ShennongSearchClient()

resp = client.snnmm.get(nmm_id="nmm-0001")
resp = client.snnmm.get(nmmsn="Artemisia annua Part-aerial")
resp = client.snnmm.get(nmmsn_zh="黄花蒿地上部")
resp = client.snnmm.get(nmmgn="Qing-hao")
resp = client.snnmm.get(nmmgn_zh="青蒿")

print(resp.total)
print(resp.results[0].snnmm.standardized_translation)
```

### Requests

```http
GET /api/snnmm?nmm_id=nmm-0001
```

```http
GET /api/snnmm?nmmsn=Artemisia%20annua%20Part-aerial
```

```http
GET /api/snnmm?nmmsn_zh=%E9%BB%84%E8%8A%B1%E8%92%BF%E5%9C%B0%E4%B8%8A%E9%83%A8
```

```http
GET /api/snnmm?nmmgn=Qing-hao
```

```http
GET /api/snnmm?nmmgn_zh=%E9%9D%92%E8%92%BF
```

### Response

Response:

```json
{
  "total": 1,
  "results": [
    {
      "nmm_id": "nmm-0001",
      "snnmm": {
        "nmm_id": "nmm-0001",
        "standardized_translation": "Artemisia annua Part-aerial (NMM-0001, Qing-hao)",
        "standardized_translation_zh": "黄花蒿地上部（NMM-0001，青蒿）",
        "nmmsn": {
          "nmmsn": "Artemisia annua Part-aerial",
          "nmmsn_zh": {
            "zh": "黄花蒿地上部",
            "pinyin": "huáng huā hāo dì shàng bù"
          },
          "nmmsn_name_element": {
            "nmm_type": "plant",
            "species_origins": [
              [
                "Artemisia annua",
                "黄花蒿"
              ]
            ],
            "medicinal_parts": [
              [
                "part aerial",
                "地上部"
              ]
            ],
            "special_descriptions": [],
            "processing_methods": []
          },
          "nmmsn_seq": [
            [
              "Artemisia annua",
              "黄花蒿"
            ],
            [
              "Part-aerial",
              "地上部"
            ],
            [
              "",
              ""
            ],
            [
              "",
              ""
            ]
          ],
          "nmmsn_explanation": "{{langs|zh|en}}\n\n根据《中国药典·2020年版·一部》记载：本天然药材为菊科植物黄花蒿*Artemisia annua* L.的干燥地上部分。秋季花盛开时釆割，除去老茎，阴干。\nAccording to the *Chinese Pharmacopoeia: 2020 edition: Volume I*, this NMM is the dried aerial part of the plant *Artemisia annua* L. of the family *Asteraceae*. It is harvested when the flowers are in full bloom in autumn, the old stems are removed, and it is dried in the shade."
        },
        "nmmgn": {
          "nmmgn": "Qing-hao",
          "nmmgn_zh": {
            "zh": "青蒿",
            "pinyin": "qīng hāo"
          },
          "nmmgn_explanation": "{{langs|zh|en}}\n\nNMMGN衍生自《中国药典·2020年版·一部》相关中药材中文名。\nNMMGN follows the Chinese name of the relevant Chinese medicinal materials in the *Chinese Pharmacopoeia: 2020 edition: Volume I*."
        }
      },
      "nmm_hierarchy": {
        "parent_nmm_id": null
      }
    }
  ]
}
```
