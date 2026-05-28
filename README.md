# Testes da API

[![Tests](https://github.com/lucasleite-charth/testesdaApi/actions/workflows/tests.yml/badge.svg)](https://github.com/lucasleite-charth/testesdaApi/actions/workflows/tests.yml)

API simples criada com FastAPI e coberta por testes automatizados com pytest.

## Estrutura

- `app/main.py`: define a aplicacao FastAPI e os endpoints `GET /` e `GET /health`.
- `tests/conftest.py`: cria fixtures de teste para importar a API e montar um cliente HTTP.
- `tests/test_api_contract.py`: valida o contrato basico da API.
- `.github/workflows/tests.yml`: executa os testes automaticamente no GitHub Actions.
- `pytest.ini`: configura a descoberta dos testes.

## Instalar dependencias

Na raiz do projeto:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Rodar a API

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Depois acesse:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/docs

## Rodar os testes

```powershell
.\.venv\Scripts\python.exe -m pytest
```

Resultado esperado:

```text
3 passed
```

## GitHub Actions

Os testes rodam automaticamente em cada `push` e `pull_request` para a branch `main`.
