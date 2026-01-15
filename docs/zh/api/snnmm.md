---
title: SNNMM 查询接口
---

# SNNMM 查询接口

Base URL: `https://shennongalpha.westlake.edu.cn`

## GET /api/snnmm

用于按系统名/通用名/ID 查询天然药材系统命名法（SNNMM）信息。每次请求只能提供一个查询参数。

### Query 参数

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `nmm_id` | 否 | 天然药材 ID，例如 `nmm-0001` |
| `nmmsn` | 否 | 系统名（英文） |
| `nmmsn_zh` | 否 | 系统名（中文） |
| `nmmgn` | 否 | 通用名（英文） |
| `nmmgn_zh` | 否 | 通用名（中文） |

以上参数必须且只能提供一个，否则返回 400。

### 响应结构

```json
{
  "total": 0,
  "results": []
}
```

`results` 中每条记录包含 `snnmm`、`nmm_hierarchy`、`synonyms` 等字段。

### Python 调用示例

```python
from shennongsearch import ShennongSearchClient

client = ShennongSearchClient()

resp = client.snnmm.get(nmm_id="nmm-0001")
resp = client.snnmm.get(nmmsn="Artemisia annua Part-aerial")
resp = client.snnmm.get(nmmsn_zh="黄花蒿地上部")
resp = client.snnmm.get(nmmgn="Qing-hao")
resp = client.snnmm.get(nmmgn_zh="青蒿")

print(resp.total)
```

### 请求示例

```http
GET /api/snnmm?nmmsn=Artemisia%20annua%20Part-aerial
```

```http
GET /api/snnmm?nmmsn_zh=黄花蒿地上部
```

```http
GET /api/snnmm?nmmgn=Qing-hao
```

```http
GET /api/snnmm?nmmgn_zh=青蒿
```

### 响应示例

响应示例：

```json
{
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
