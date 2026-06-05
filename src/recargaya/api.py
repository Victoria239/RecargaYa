from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from recargaya.calculadora import calcular_recarga


app = FastAPI(
    title="RecargaYa API",
    description="API para calcular el valor final de recargas de celular",
    version="1.0.0",
)


class RecargaRequest(BaseModel):
    monto: int
    premium: bool = False


@app.get("/")
def home():
    return {"mensaje": "API RecargaYa funcionando correctamente"}


@app.post("/recargas/calcular")
def calcular(request: RecargaRequest):
    try:
        return calcular_recarga(request.monto, request.premium)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))