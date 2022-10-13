from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from server.infra.sqlalchemy.repositorios.dominio import RepositorioDominio
from server.infra.sqlalchemy.config.database import get_db, criar_bd
from server.schemas.schemas import Dominio


criar_bd()

app = FastAPI(debug=True)

@app.post('/dominios')
def criar_dominios(dominio: Dominio, db: Session = Depends(get_db)):
    dominio_criado = RepositorioDominio(db).criar(dominio)
    return dominio_criado

@app.get('/dominios')
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