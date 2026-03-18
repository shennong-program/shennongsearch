# shennongsearch

Python SDK for ShennongAlpha search APIs.

## Install

With uv:

```bash
uv sync
```

With pip:

```bash
pip install -e .
```

## Quickstart

```python
from shennongsearch import ShennongSearchClient

client = ShennongSearchClient()

resp = client.name.species_origins.search(q="Ephedra sinica", page=1, limit=1)
print(resp.results[0].la, resp.results[0].zh)

snnmm = client.snnmm.get(nmmsn="Example System Name")
print(snnmm.results[0].snnmm.standardized_translation)
```

## Configuration

```python
client = ShennongSearchClient(
    base_url="https://shennongalpha.westlake.edu.cn",
    timeout=10.0,
)
```

## API Docs

Chinese docs: `docs/zh/api/name.md`, `docs/zh/api/snnmm.md`.
English docs: `docs/en/api/name.md`, `docs/en/api/snnmm.md`.

## Tests

```bash
uv sync --extra dev
# Test against https://shennongalpha.westlake.edu.cn
uv run pytest -m api

# Local dev
SHENNONGALPHA_BASE_URL=http://localhost:4000 uv run pytest -m api
```

## Docs (VitePress)

```bash
cd docs
pnpm install
pnpm dev
```
