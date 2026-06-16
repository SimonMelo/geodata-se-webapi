from fastapi import APIRouter, HTTPException
from app.services import ibge

router = APIRouter(prefix="/municipios", tags=["Municípios"])

@router.get("/")
async def listar_municipios():
    return await ibge.get_municipios()

@router.get("/{municipio_id}/bairros")
async def listar_bairros(municipio_id: int):
    data = await ibge.get_bairros(municipio_id)
    if not data:
        raise HTTPException(status_code=404, detail="Município não encontrado")
    return data