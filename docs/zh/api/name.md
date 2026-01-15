---
title: Name 查询接口
---

# Name 查询接口

Base URL: `https://shennongalpha.westlake.edu.cn`

## name_type 枚举

| 值 | 含义 |
| --- | --- |
| `species_origins` | 物种基源 |
| `medicinal_parts` | 用药部位 |
| `processing_methods` | 炮制方法 |
| `special_descriptions` | 特殊形容 |

## GET /api/name/search

用于列表搜索（全文检索）。`q` 为空时返回默认排序列表。

### Query 参数

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `name_type` | 是 | 见上方枚举 |
| `q` | 否 | 搜索关键词，默认空字符串 |
| `page` | 否 | 页码，默认 `1` |
| `limit` | 否 | 每页数量，默认 `20` |

### 响应结构

```json
{
  "q": "",
  "page": 1,
  "limit": 20,
  "total": 0,
  "results": []
}
```

`results` 的结构会随 `name_type` 不同而变化：

- `species_origins`：包含 `la`/`zh` 等物种字段
- `medicinal_parts`：包含 `en`、`zh`、`explanation` 等用药部位字段
- `processing_methods`：包含 `en`、`zh`、`en_full`、`category` 等炮制方法字段
- `special_descriptions`：包含 `en`、`zh`、`explanation` 等特殊形容字段

### Python 调用示例

```python
from shennongsearch import ShennongSearchClient
from shennongsearch.models import NameType

client = ShennongSearchClient()

resp = client.name.search(NameType.MEDICINAL_PARTS, q="stem herbaceous", page=1, limit=1)
print(resp.results[0].en, resp.results[0].zh)
```

### 示例（按 name_type）

以下示例为真实请求结果的截取（`limit=1`），用于展示关键字段。

#### species_origins

请求示例（英文）：

```http
GET /api/name/search?name_type=species_origins&q=Ephedra%20sinica&page=1&limit=1
```

响应示例（英文查询）：

```json
{
  "q": "Ephedra sinica",
  "page": 1,
  "limit": 1,
  "results": [
    {
      "la": "Ephedra sinica",
      "zh": "草麻黄",
      "std": true,
      "refs": [
        {
          "db": "sp2000",
          "id": "T20171000011148",
          "la": "Ephedra sinica",
          "zh": "草麻黄",
          "url": "http://www.sp2000.org.cn/species/show_species_details/T20171000011148"
        }
      ]
    }
  ]
}
```

请求示例（中文）：

```http
GET /api/name/search?name_type=species_origins&q=草麻黄&page=1&limit=1
```

响应示例（中文查询）：

```json
{
  "q": "草麻黄",
  "page": 1,
  "limit": 1,
  "results": [
    {
      "la": "Ephedra sinica",
      "zh": "草麻黄",
      "std": true,
      "refs": [
        {
          "db": "sp2000",
          "id": "T20171000011148",
          "la": "Ephedra sinica",
          "zh": "草麻黄",
          "url": "http://www.sp2000.org.cn/species/show_species_details/T20171000011148"
        }
      ]
    }
  ]
}
```

#### medicinal_parts

请求示例（英文）：

```http
GET /api/name/search?name_type=medicinal_parts&q=stem%20herbaceous&page=1&limit=1
```

响应示例（英文查询）：

```json
{
  "q": "stem herbaceous",
  "page": 1,
  "limit": 1,
  "results": [
    {
      "en": "stem herbaceous",
      "zh": "草质茎",
      "explanation": "{{langs|zh|en}}\n\n草质的茎\nHerbaceous Stem"
    }
  ]
}
```

请求示例（中文）：

```http
GET /api/name/search?name_type=medicinal_parts&q=草质茎&page=1&limit=1
```

响应示例（中文查询）：

```json
{
  "q": "草质茎",
  "page": 1,
  "limit": 1,
  "results": [
    {
      "en": "stem herbaceous",
      "zh": "草质茎",
      "explanation": "{{langs|zh|en}}\n\n草质的茎\nHerbaceous Stem"
    }
  ]
}
```

#### processing_methods

请求示例（英文）：

```http
GET /api/name/search?name_type=processing_methods&q=segmented&page=1&limit=1
```

响应示例（英文查询）：

```json
{
  "q": "segmented",
  "page": 1,
  "limit": 1,
  "results": [
    {
      "en": "segmented",
      "zh": "段制",
      "en_full": "processed by segmenting",
      "category": {
        "major": "cutted (切制)",
        "minor": "segmented (段制)"
      },
      "explanation": "{{langs|zh|en}}\n\n切段，或使成段状。根据中华人民共和国药典2020版四部0213炮制通则。\nCut into sections, or made into segment shapes. According to the General Rules for Processing in the 2020 edition of the Pharmacopoeia of the People's Republic of China, section 0213."
    }
  ]
}
```

请求示例（中文）：

```http
GET /api/name/search?name_type=processing_methods&q=段制&page=1&limit=1
```

响应示例（中文查询）：

```json
{
  "q": "段制",
  "page": 1,
  "limit": 1,
  "results": [
    {
      "en": "segmented",
      "zh": "段制",
      "en_full": "processed by segmenting",
      "category": {
        "major": "cutted (切制)",
        "minor": "segmented (段制)"
      },
      "explanation": "{{langs|zh|en}}\n\n切段，或使成段状。根据中华人民共和国药典2020版四部0213炮制通则。\n Cut into sections, or made into segment shapes. According to the General Rules for Processing in the 2020 edition of the Pharmacopoeia of the People's Republic of China, section 0213."
    }
  ]
}
```

#### special_descriptions

请求示例（英文）：

```http
GET /api/name/search?name_type=special_descriptions&q=black&page=1&limit=1
```

响应示例（英文查询）：

```json
{
  "q": "black",
  "page": 1,
  "limit": 1,
  "results": [
    {
      "en": "black",
      "zh": "黑",
      "explanation": "{{langs|zh|en}}\n\n黑色的。\nBlack."
    }
  ]
}
```

请求示例（中文）：

```http
GET /api/name/search?name_type=special_descriptions&q=黑&page=1&limit=1
```

响应示例（中文查询）：

```json
{
  "q": "黑",
  "page": 1,
  "limit": 1,
  "results": [
    {
      "en": "black",
      "zh": "黑",
      "explanation": "{{langs|zh|en}}\n\n黑色的。\nBlack."
    }
  ]
}
```
