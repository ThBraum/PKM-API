from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from server.schemas import schemas
from server.infra.sqlalchemy.models import models
from sqlalchemy import select, delete, update

class RepositorioDominio():
    def __init__(self, session: Session):
        self.session = session


    def criar(self, dominio: schemas.Dominio):
        session_dominio = models.Dominio(descricao=dominio.descricao, 
                                    valor=dominio.valor)
        self.session.add(session_dominio)
        self.session.commit()
        self.session.refresh(session_dominio)
        return session_dominio

    def listar(self):
        stmt = select(models.Dominio)
        row = self.session.execute(stmt).scalars().all()
        return row

    def obter(self, dominio_id: int):
        stmt = select(models.Dominio).filter_by(id=dominio_id)
        #if models.Dominio.id != dominio_id:
        #    raise HTTPException(
        #        status_code=status.HTTP_404_NOT_FOUND, detail=f'Dominio de id: {dominio_id} não encontrado'
        #    )
        obt_dominio = self.session.execute(stmt).scalars().all()
        return obt_dominio

    def remover(self, dominio_id: int):
        stmt = delete(models.Dominio).where(models.Dominio.id == dominio_id)
        
        self.session.execute(stmt)
        self.session.commit()
        #self.session.refresh(del_dominio)

    def editar(self, dominio: schemas.Dominio):
        stmt = update(models.Dominio).where(
            models.Dominio.id == dominio.id
            ).values(descricao=dominio.descricao, 
                    valor=dominio.valor
            )
        self.session.execute(stmt)
        self.session.commit()