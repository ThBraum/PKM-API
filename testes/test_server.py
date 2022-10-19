from urllib import response
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, false
from sqlalchemy.orm import sessionmaker
from server.infra.sqlalchemy.config.database import Base, get_db
from server.server import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_post_dominios_201():
    response = client.post('/dominios', json={
        "descricao": "veneno",
        "valor": 1
    })
    assert response.status_code == 201, response.text
    assert response.json()["descricao"] == "veneno"
    assert response.json()["valor"] == 1

def test_get_dominios_200():
    response = client.get('/dominios')
    assert response.status_code == 200, response.text

def test_get_dominios_by_id_200():
    dominio_id = 1
    response = client.get(f'/dominios/{dominio_id}')
    assert response.status_code == 200, response.text

def test_get_dominios_by_id_422():
    dominio_id = 23.4
    response = client.get(f'/dominios/{dominio_id}')
    assert response.status_code == 422, response.text

def test_delete_dominios_by_id_200():
    dominio_id = 5
    response = client.delete(f'/dominios/{dominio_id}')
    assert response.status_code == 200, response.text

def test_update_dominios_by_id_200():
    response = client.put('/dominios', json={
        "descricao": "planta",
        "valor": 2,
        "id": 11
    })
    assert response.json() == {
        "descricao": "planta",
        "valor": 2,
        "id": 11
    }
    assert response.status_code == 200, response.text

#----------------------

def test_post_treinadores_201():
    response = client.post('/treinadores', json={
        "nome": "ash",
        "lider_ginasio": False,
        "descricao": "fire red",
        "qt_insignias": 2,
        "qt_pokemons": 11
    })
    assert response.status_code == 201, response.text
    assert response.json()["lider_ginasio"] == False
    assert response.json()["descricao"] == "fire red"
    assert response.json()["qt_pokemons"] == 11

def test_get_treinadores_200():
    response = client.get('/treinadores')
    assert response.status_code == 200, response.text

def test_get_treinadores_by_id_200():
    treinador_id = 1
    response = client.get(f'/treinadores/{treinador_id}')
    assert response.status_code == 200, response.text

def test_get_treinadores_by_id_422():
    treinador_id = 1.3
    response = client.get(f'/treinadores/{treinador_id}')
    assert response.status_code == 422, response.text

def test_delete_treinadores_by_id_200():
    treinador_id = 5
    response = client.delete(f'/treinadores/{treinador_id}')
    assert response.status_code == 200, response.text

def test_update_treinadores_by_id_200():
    response = client.put('/treinadores', json={
        "id": 2,
        "nome": "brock",
        "lider_ginasio": True,
        "descricao": "black and white",
        "qt_insignias": 5,
        "qt_pokemons": 18
    })
    assert response.json() == {
        "id": 2,
        "nome": "brock",
        "lider_ginasio": True,
        "descricao": "black and white",
        "qt_insignias": 5,
        "qt_pokemons": 18
    }
    assert response.status_code == 200, response.text

#------------------------

def test_post_pokemons_201():
    response = client.post('/pokemons', json={
        "nome": "ponyta",
        "forma": 1,
        "treinador": "misty",
        "tipo": "fogo"
    })
    assert response.status_code == 201, response.text
    assert response.json()["forma"] == 1
    assert response.json()["tipo"] == "fogo"

def test_get_pokemons_200():
    response = client.get('/pokemons')
    assert response.status_code == 200, response.text

def test_get_pokemons_by_id_200():
    pokemon_id = 1
    response = client.get(f'/pokemons/{pokemon_id}')
    assert response.status_code == 200, response.text

def test_get_pokemons_by_id_422():
    pokemon_id = 9.8
    response = client.get(f'/pokemons/{pokemon_id}')
    assert response.status_code == 422, response.text

def test_delete_pokemons_by_id_200():
    pokemon_id = 6
    response = client.delete(f'/pokemons/{pokemon_id}')
    assert response.status_code == 200, response.text

def test_update_pokemon_by_id_200():
    response = client.put('/pokemons', json={
        "id": 2,
        "nome": "eevee",
        "forma": 1,
        "treinador": "misty",
        "tipo": "normal"
    })
    assert response.json() == {
        "id": 2,
        "nome": "eevee",
        "forma": 1,
        "treinador": "misty",
        "tipo": "normal"
    }
    assert response.status_code == 200, response.text