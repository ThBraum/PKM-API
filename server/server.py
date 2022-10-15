from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from server.infra.sqlalchemy.repositorios.dominio import RepositorioDominio
from server.infra.sqlalchemy.repositorios.treinador import RepositorioTreinador
from server.infra.sqlalchemy.config.database import get_db, criar_bd
from server.schemas.schemas import *

#criar_bd()

app = FastAPI(debug=True)

@app.post('/dominios', status_code=status.HTTP_201_CREATED)
def criar_dominios(dominio: Dominio, db: Session = Depends(get_db)):
    dominio_criado = RepositorioDominio(db).criar(dominio)
    return dominio_criado

@app.get('/dominios', status_code=status.HTTP_200_OK)
def listar_dominios(db: Session = Depends(get_db)):
    dominios = RepositorioDominio(db).listar()
    return dominios
    
@app.get('/dominios/{dominio_id}')
def obter_dominio(dominio_id: int, db: Session = Depends(get_db)):
    obt_dominio = RepositorioDominio(db).obter(dominio_id)
    return obt_dominio

@app.delete('/dominios/{dominio_id}')
def excluir_dominio(dominio_id: int, db: Session = Depends(get_db)):
    obt_dominio = RepositorioDominio(db).remover(dominio_id)
    return {"mensagem": f"Registro de id={dominio_id} removido"}

@app.post('/treinadores', status_code=status.HTTP_201_CREATED)
def criar_treinadores(treinador: Treinador, db: Session = Depends(get_db)):
    treinador_criado = RepositorioTreinador(db).criar(treinador)
    return treinador_criado

@app.get('/treinadores', status_code=status.HTTP_200_OK)
def listar_treinadores(db: Session = Depends(get_db)):
    treinadores = RepositorioTreinador(db).listar()
    return treinadores

@app.get('/treinadores/{treinador_id}')
def obter_treinador(treinador_id: int, db: Session = Depends(get_db)):
    obt_treinador = RepositorioTreinador(db).obter(treinador_id)
    return obt_treinador

@app.delete('/treinadores/{treinador_id}')
def excluir_treinador(treinador_id: int, db: Session = Depends(get_db)):
    obt_treinador = RepositorioTreinador(db).remover(treinador_id)
    return {"mensagem": f"Registro de id={treinador_id} removido"}