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

按类型调用对应子 API（以下示例复用同一个 client）：

```python
from shennongsearch import ShennongSearchClient

client = ShennongSearchClient()
```

#### species_origins

```python
resp = client.name.species_origins.search(q="Ephedra sinica", page=1, limit=1)
print(resp.results[0].la, resp.results[0].zh)
```

#### medicinal_parts

```python
resp = client.name.medicinal_parts.search(q="stem herbaceous", page=1, limit=1)
print(resp.results[0].en, resp.results[0].zh)
```

#### processing_methods

```python
resp = client.name.processing_methods.search(q="segmented", page=1, limit=1)
print(resp.results[0].en, resp.results[0].zh)
```

#### special_descriptions

```python
resp = client.name.special_descriptions.search(q="black", page=1, limit=1)
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

## GET /api/name/all

用于一次性获取指定 `name_type` 的全量列表（不分页），适合小规模数据的一键下载。
由于物种数据量较大，建议使用搜索端口进行查询，因此仅提供下面 3 类。

目前仅开放以下 `name_type`：

- `medicinal_parts`
- `special_descriptions`
- `processing_methods`

### Query 参数

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `name_type` | 是 | 仅支持上方三类 |

### 响应结构

响应结构与 `/api/name/search` 一致，`q` 固定为空字符串，`page` 固定为 `1`，`limit` 等于返回数量。

```json
{
  "q": "",
  "page": 1,
  "limit": 0,
  "total": 0,
  "results": []
}
```

### Python 调用示例

```python
from shennongsearch import ShennongSearchClient

client = ShennongSearchClient()

resp = client.name.medicinal_parts.all()
print(resp.total, len(resp.results))
```

如需返回 pandas DataFrame：

```python
df = client.name.medicinal_parts.all_dataframe()
print(df.head())
```

#### medicinal_parts

调用示例：

```python
resp = client.name.medicinal_parts.all()
print(resp.results[0].en, resp.results[0].zh)
```

表结构（DataFrame 仅返回以下列）：

| 列 | 类型 | 说明 |
| --- | --- | --- |
| `en` | `string` | 英文 |
| `zh` | `string` | 中文 |
| `explanation` | `string` | 解释 |

#### special_descriptions

调用示例：

```python
resp = client.name.special_descriptions.all()
print(resp.results[0].en, resp.results[0].zh)
```

表结构（DataFrame 仅返回以下列）：

| 列 | 类型 | 说明 |
| --- | --- | --- |
| `en` | `string` | 英文 |
| `zh` | `string` | 中文 |
| `explanation` | `string` | 解释 |

#### processing_methods

调用示例：

```python
resp = client.name.processing_methods.all()
print(resp.results[0].en, resp.results[0].zh)
```

表结构（DataFrame 仅返回以下列）：

| 列 | 类型 | 说明 |
| --- | --- | --- |
| `en` | `string` | 英文 |
| `zh` | `string` | 中文 |
| `en_full` | `string` | 英文全称 |
| `category_major` | `string` | 分类一级（来自 `category.major`） |
| `category_minor` | `string` | 分类二级（来自 `category.minor`） |
| `explanation` | `string` | 解释 |

### 请求示例

```http
GET /api/name/all?name_type=medicinal_parts
```

### 响应示例

```json
{
  "q": "",
  "page": 1,
  "limit": 1,
  "total": 1,
  "results": [
    {
      "en": "stem herbaceous",
      "zh": "草质茎",
      "explanation": "{{langs|zh|en}}\n\n草质的茎\nHerbaceous Stem"
    }
  ]
}
```
