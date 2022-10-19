from ast import Try
from logging import exception
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from server.infra.sqlalchemy.repositorios.repositorio_dominio import RepositorioDominio
from server.infra.sqlalchemy.repositorios.repositorio_treinador import RepositorioTreinador
from server.infra.sqlalchemy.repositorios.repositorio_pokemon import RepositorioPokemon
from server.infra.sqlalchemy.config.database import get_db, criar_bd
from server.schemas.schemas import *
from typing import List

#criar_bd()

app = FastAPI(debug=True)

@app.get('/')
async def read_root():
    return {"msg": "Hello World"}


#DOMINIOS

@app.post('/dominios', status_code=status.HTTP_201_CREATED, tags=["Post Methods"])
def criar_dominios(dominio: Dominio, db: Session = Depends(get_db)):
    dominio_criado = RepositorioDominio(db).criar(dominio)
    return dominio_criado

@app.get('/dominios', status_code=status.HTTP_200_OK, tags=["Get Methods - List"])
def listar_dominios(db: Session = Depends(get_db)):
    dominios = RepositorioDominio(db).listar()
    return dominios
    
@app.get('/dominios/{dominio_id}', tags=["Get Methods - Get By ID"])
def obter_dominio(dominio_id: int, db: Session = Depends(get_db)):
    obt_dominio = RepositorioDominio(db).obter(dominio_id)
    return obt_dominio

@app.delete('/dominios/{dominio_id}', tags=["Delete Methods"])
def excluir_dominio(dominio_id: int, db: Session = Depends(get_db)):
    obt_dominio = RepositorioDominio(db).remover(dominio_id)
    return {"mensagem": f"Registro de id={dominio_id} removido"}

@app.put('/dominios', status_code=status.HTTP_200_OK, tags=["Put Methods"])
def atualizar_dominios(dominio: Dominio, db: Session = Depends(get_db)):
    try:
        dominio_para_att = RepositorioDominio(db).obter(dominio.id)
        if dominio_para_att:
            RepositorioDominio(db).editar(dominio)
        dominio_atualizado = RepositorioDominio(db).obter(dominio.id)
        return dominio_atualizado
    except Exception as exception:
        raise exception

#------------------------------------


#TREINADORES

@app.post('/treinadores', status_code=status.HTTP_201_CREATED, tags=["Post Methods"])
def criar_treinadores(treinador: Treinador, db: Session = Depends(get_db)):
    treinador_criado = RepositorioTreinador(db).criar(treinador)
    return treinador_criado

@app.get('/treinadores', status_code=status.HTTP_200_OK, tags=["Get Methods - List"])
def listar_treinadores(db: Session = Depends(get_db)):
    treinadores = RepositorioTreinador(db).listar()
    return treinadores

@app.get('/treinadores/{treinador_id}', tags=["Get Methods - Get By ID"])
def obter_treinador(treinador_id: int, db: Session = Depends(get_db)):
    obt_treinador = RepositorioTreinador(db).obter(treinador_id)
    return obt_treinador

@app.delete('/treinadores/{treinador_id}', tags=["Delete Methods"])
def excluir_treinador(treinador_id: int, db: Session = Depends(get_db)):
    obt_treinador = RepositorioTreinador(db).remover(treinador_id)
    return {"mensagem": f"Registro de id={treinador_id} removido"}

@app.put('/treinadores', status_code=status.HTTP_200_OK, tags=["Put Methods"])
def atualizar_treinadores(treinador: Treinador, db: Session = Depends(get_db)):
    try:
        treinador_para_att = RepositorioTreinador(db).obter(treinador.id)
        if treinador_para_att:
            RepositorioTreinador(db).editar(treinador)
        treinador_atualizado = RepositorioTreinador(db).obter(treinador.id)
        return treinador_atualizado
    except Exception as exception:
        raise exception
#------------------------------------


#POKEMONS

@app.post('/pokemons', status_code=status.HTTP_201_CREATED, tags=["Post Methods"])
def criar_pokemons(pokemon: Pokemon, db: Session = Depends(get_db)):
    pokemon_criado = RepositorioPokemon(db).criar(pokemon)
    return pokemon_criado

@app.get('/pokemons', status_code=status.HTTP_200_OK, tags=["Get Methods - List"])
def listar_pokemons(db: Session = Depends(get_db)):
    pokemons = RepositorioPokemon(db).listar()
    return pokemons

@app.get('/pokemons/{pokemon_id}', tags=["Get Methods - Get By ID"])
def obter_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    obt_pokemon = RepositorioPokemon(db).obter(pokemon_id)
    return obt_pokemon

@app.delete('/pokemons/{pokemon_id}', tags=["Delete Methods"])
def excluir_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    obt_pokemon = RepositorioPokemon(db).remover(pokemon_id)
    return {"mensagem": f"Registro de id={pokemon_id} removido"}


@app.put('/pokemons', status_code=status.HTTP_200_OK, tags=["Put Methods"])
def atualizar_pokemons(pokemon: Pokemon, db: Session = Depends(get_db)):
    try:
        pokemon_para_att = RepositorioPokemon(db).obter(pokemon.id)
        if pokemon_para_att:
            RepositorioPokemon(db).editar(pokemon)
        pokemon_atualizado = RepositorioPokemon(db).obter(pokemon.id)
        return pokemon_atualizado
    except Exception as exception:
        return exception

