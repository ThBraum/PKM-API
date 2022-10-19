from pyexpat import model
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from server.infra.sqlalchemy.models import models
from server.schemas import schemas
from sqlalchemy import select, delete, update

class RepositorioTreinador():
    def __init__(self, session: Session):
        self.session = session

    def criar(self, treinador: schemas.Treinador):
        session_treinador = models.Treinador(nome=treinador.nome, 
                                            lider_ginasio=treinador.lider_ginasio,
                                            descricao=treinador.descricao,
                                            qt_insignias=treinador.qt_insignias,
                                            qt_pokemons=treinador.qt_pokemons)

        self.session.add(session_treinador)
        self.session.commit()
        self.session.refresh(session_treinador)
        return session_treinador

    def listar(self):
        stmt = select(models.Treinador)
        row = self.session.execute(stmt).scalars().all()
        return row

    def obter(self, treinador_id: int):
        #stmt = select(models.Treinador).filter_by(id=treinador_id)
        #obt_treinador = self.session.execute(stmt).one()
        #return obt_treinador

        stmt = select(models.Treinador).filter_by(id=treinador_id)
        #if models.Treinador.id != treinador_id:
        #    raise HTTPException(
        #        status_code=status.HTTP_404_NOT_FOUND, detail=f'Dominio de id: {treinador_id} não encontrado'
        #    )
        row = self.session.execute(stmt).scalars().first()
        return row

    def remover(self, treinador_id: int):
        stmt = delete(models.Treinador).where(models.Treinador.id == treinador_id)
        
        self.session.execute(stmt)
        self.session.commit()

    def editar(self, treinador: schemas.Treinador):
        stmt = update(models.Treinador).where(
            models.Treinador.id == treinador.id
        ).values(
            nome=treinador.nome, 
            lider_ginasio=treinador.lider_ginasio,
            descricao=treinador.descricao,
            qt_insignias=treinador.qt_insignias,
            qt_pokemons=treinador.qt_pokemons
        )
        self.session.execute(stmt)
        self.session.commit()
