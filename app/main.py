from fastapi import FastAPI


app = FastAPI(title="Testes da API")


@app.get("/")
def read_root():
    return {"message": "API funcionando"}


@app.get("/health")
def read_health():
    return {"status": "ok"}
