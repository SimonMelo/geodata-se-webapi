from fastapi import FastAPI
from app.routers import municipios, cep

app = FastAPI(
    title="Sergipe WebAPI",
    description="API para consulta de dados geográficos de Sergipe",
    version="1.0.0"
)

app.include_router(cep.router)
app.include_router(municipios.router)

@app.get("/")
def root():
    return {"message": "Bem-vindo à API de Sergipe!"}