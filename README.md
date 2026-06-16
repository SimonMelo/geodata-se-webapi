# 🗺️ Geodata SE WebAPI

Uma WebAPI de dados geográficos do estado de Sergipe. Centraliza informações de municípios, bairros e CEPs em um único lugar, facilitando o desenvolvimento de aplicações focadas em Sergipe.

## Por que existe?

Precisei de uma WebAPI geográfica focada em Sergipe para um projeto pessoal e não encontrei nada centralizado — só o IBGE e o ViaCEP separados. Resolvi construir até mesmo por aprendizado.

## Stack

- **Python 3.13**
- **FastAPI**
- **ViaCEP** — endereços por CEP
- **IBGE API** — municípios
- **Nominatim (OpenStreetMap)** — geocoding (lat/lng)

## Endpoints

### `GET /municipios`
Lista todos os 75 municípios de Sergipe.

```json
[
  { "id": 2800308, "nome": "Aracaju" },
  { "id": 2803500, "nome": "Lagarto" }
]
```

---

### `GET /municipios/{id}/bairros`
Retorna os bairros de um município pelo código IBGE.

```
GET /municipios/2800308/bairros
```

```json
{
  "municipio": "Aracaju",
  "bairros": ["Atalaia", "Centro", "Farolândia", "Jardins", "Luzia", "..."]
}
```

---

### `GET /cep/{cep}`
Busca endereço completo com coordenadas geográficas. Aceita CEP com ou sem traço. Restrito a CEPs de Sergipe.

```
GET /cep/49048-010
```

```json
{
  "zipCode": "49048-010",
  "street": "Avenida Adélia Franco",
  "neighborhood": "Luzia",
  "city": "Aracaju",
  "state": "SE",
  "country": "Brasil",
  "latitude": -10.9427963,
  "longitude": -37.0678241
}
```

## Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/sergipe-api.git
cd sergipe-api

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\Activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Suba o servidor
uvicorn app.main:app --reload
```

Acesse `http://localhost:8000/docs` para a documentação interativa.

## Falta algum bairro?

Os dados de bairros são mantidos em [`app/data/bairros.json`](app/data/bairros.json). Se perceber que falta algum bairro do seu município, abre uma issue ou manda um PR — a ideia é construir isso junto com a comunidade sergipana. 🟡