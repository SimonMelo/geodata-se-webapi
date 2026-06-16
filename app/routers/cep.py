from fastapi import APIRouter, HTTPException
from app.services import viacep, nominatim

router = APIRouter(prefix="/cep", tags=["CEP"])

@router.get("/{cep}", summary="Consultar endereço por CEP")
async def consultar_cep(cep: str):
    endereco = await viacep.get_endereco(cep)
    
    if not endereco:
        raise HTTPException(status_code=404, detail="CEP não encontrado")
    
    if endereco["state"] != "SE":
        raise HTTPException(status_code=400, detail="CEP não pertence a Sergipe")

    query = f"{endereco['street']}, {endereco['neighborhood']}, {endereco['city']}, Sergipe, Brasil"
    coordenadas = await nominatim.get_coordenadas(query)

    return {**endereco, **(coordenadas or {})}
