---
title: Name Query API
---

# Name Query API

Base URL: `https://shennongalpha.westlake.edu.cn`

## name_type enum

| Value | Meaning |
| --- | --- |
| `species_origins` | Species origin |
| `medicinal_parts` | Medicinal part |
| `processing_methods` | Processing method |
| `special_descriptions` | Special description |

## GET /api/name/search

Full-text search for list queries. When `q` is empty, it returns the default sorted list.

### Query parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `name_type` | Yes | See enum above |
| `q` | No | Search keyword, default empty |
| `page` | No | Page number, default `1` |
| `limit` | No | Page size, default `20` |

### Response

```json
{
  "q": "",
  "page": 1,
  "limit": 20,
  "total": 0,
  "results": []
}
```

`results` fields vary by `name_type`:

- `species_origins`: contains `la`/`zh` and other species fields
- `medicinal_parts`: contains `en`, `zh`, `explanation`, etc.
- `processing_methods`: contains `en`, `zh`, `en_full`, `category`, etc.
- `special_descriptions`: contains `en`, `zh`, `explanation`, etc.

### Python Usage

```python
from shennongsearch import ShennongSearchClient
from shennongsearch.models import NameType

client = ShennongSearchClient()

resp = client.name.search(NameType.MEDICINAL_PARTS, q="stem herbaceous", page=1, limit=1)
print(resp.results[0].en, resp.results[0].zh)
```


### Examples by name_type

The examples below are trimmed from real responses (`limit=1`) to highlight key fields.

#### species_origins

Request (English):

```http
GET /api/name/search?name_type=species_origins&q=Ephedra%20sinica&page=1&limit=1
```

Response (English query):

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

Request (Chinese):

```http
GET /api/name/search?name_type=species_origins&q=草麻黄&page=1&limit=1
```

Response (Chinese query):

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

Request (English):

```http
GET /api/name/search?name_type=medicinal_parts&q=stem%20herbaceous&page=1&limit=1
```

Response (English query):

```json
{
  "q": "stem herbaceous",
  "page": 1,
  "limit": 1,
  "results": [
    {
      "en": "stem herbaceous",
      "zh": "草质茎",
      "explanation": "{{langs|zh|en}}\n\n草质的茎 \n Grassy Stem"
    }
  ]
}
```

Request (Chinese):

```http
GET /api/name/search?name_type=medicinal_parts&q=草质茎&page=1&limit=1
```

Response (Chinese query):

```json
{
  "q": "草质茎",
  "page": 1,
  "limit": 1,
  "results": [
    {
      "en": "stem herbaceous",
      "zh": "草质茎",
      "explanation": "{{langs|zh|en}}\n\n草质的茎 \n Grassy Stem"
    }
  ]
}
```

#### processing_methods

Request (English):

```http
GET /api/name/search?name_type=processing_methods&q=segmented&page=1&limit=1
```

Response (English query):

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
      "explanation": "{{langs|zh|en}}\n\n切段，或使成段状。根据中华人民共和国药典2020版四部0213炮制通则。 \n Cut into sections, or made into segment shapes. According to the General Rules for Processing in the 2020 edition of the Pharmacopoeia of the People's Republic of China, section 0213."
    }
  ]
}
```

Request (Chinese):

```http
GET /api/name/search?name_type=processing_methods&q=段制&page=1&limit=1
```

Response (Chinese query):

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
      "explanation": "{{langs|zh|en}}\n\n切段，或使成段状。根据中华人民共和国药典2020版四部0213炮制通则。 \n Cut into sections, or made into segment shapes. According to the General Rules for Processing in the 2020 edition of the Pharmacopoeia of the People's Republic of China, section 0213."
    }
  ]
}
```

#### special_descriptions

Request (English):

```http
GET /api/name/search?name_type=special_descriptions&q=black&page=1&limit=1
```

Response (English query):

```json
{
  "q": "black",
  "page": 1,
  "limit": 1,
  "results": [
    {
      "en": "black",
      "zh": "黑",
      "explanation": "{{langs|zh|en}}\n\n黑色的。 \n Black."
    }
  ]
}
```

Request (Chinese):

```http
GET /api/name/search?name_type=special_descriptions&q=黑&page=1&limit=1
```

Response (Chinese query):

```json
{
  "q": "黑",
  "page": 1,
  "limit": 1,
  "results": [
    {
      "en": "black",
      "zh": "黑",
      "explanation": "{{langs|zh|en}}\n\n黑色的。 \n Black."
    }
  ]
}
```
