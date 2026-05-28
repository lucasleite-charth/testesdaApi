from importlib import import_module
from pathlib import Path
import sys

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


@pytest.fixture(scope="session")
def api_app() -> FastAPI:
    module = import_module("app.main")
    application = getattr(module, "app", None)

    assert application is not None, (
        "app.main precisa expor uma variavel chamada `app` com a instancia da API."
    )
    assert isinstance(application, FastAPI), (
        "`app` precisa ser uma instancia de fastapi.FastAPI para usar estes testes."
    )

    return application


@pytest.fixture()
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture()
async def client(api_app: FastAPI) -> AsyncClient:
    transport = ASGITransport(app=api_app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        yield client
