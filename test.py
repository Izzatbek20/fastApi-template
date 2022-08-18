from fastapi import FastAPI
from fastapi.testclient import TestClient

test = FastAPI()


@test.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(test)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
