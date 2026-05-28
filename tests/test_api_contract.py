import pytest


pytestmark = pytest.mark.anyio


async def test_root_endpoint_returns_success_json(client):
    response = await client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")

    payload = response.json()
    assert isinstance(payload, dict)
    assert payload, "GET / deve retornar um JSON com informacoes da API."


async def test_openapi_schema_is_available(client):
    response = await client.get("/openapi.json")

    assert response.status_code == 200

    schema = response.json()
    assert schema["openapi"].startswith("3.")
    assert schema["info"]["title"]
    assert "/" in schema["paths"]
