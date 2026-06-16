import json
import httpx
from cachetools import TTLCache
from pathlib import Path

cache = TTLCache(maxsize=10, ttl=86400)

_bairros_data = None

def _carregar_bairros():
    global _bairros_data
    if _bairros_data is None:
        path = Path(__file__).parent.parent / "data" / "bairros.json"
        with open(path, encoding="utf-8") as f:
            _bairros_data = json.load(f)
    return _bairros_data

async def get_municipios():
    if "municipios" in cache:
        return cache["municipios"]
    async with httpx.AsyncClient() as client:
        r = await client.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/28/municipios")
        data = [{"id": m["id"], "nome": m["nome"]} for m in r.json()]
        cache["municipios"] = data
        return data

async def get_bairros(municipio_id: int):
    bairros = _carregar_bairros()
    municipio = bairros.get(str(municipio_id))
    if not municipio:
        return None
    return municipio