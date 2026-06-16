import httpx

async def get_endereco(cep: str):
    cep = cep.replace("-", "").strip()
    url = f"https://viacep.com.br/ws/{cep}/json/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        if "erro" in data:
            return None
        return {
            "zipCode":      data.get("cep"),
            "street":       data.get("logradouro"),
            "neighborhood": data.get("bairro"),
            "city":         data.get("localidade"),
            "state":        data.get("uf"),
            "country":      "Brasil",
        }