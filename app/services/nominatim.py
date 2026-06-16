import httpx

async def get_coordenadas(endereco: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": endereco, "format": "json", "limit": "1"},
            headers={"User-Agent": "sergipe-api/1.0"}
        )
        results = r.json()
        if not results:
            return None
        return {
            "latitude": float(results[0]["lat"]),
            "longitude": float(results[0]["lon"])
        }