from sqlalchemy.orm import Session
from server.schemas import schemas
from server.infra.sqlalchemy.models import models
from sqlalchemy import select, delete

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
        dominios = self.session.query(models.Dominio).all()
        return dominios

    def obter(self, dominio_id: int):
        stmt = select(models.Dominio).filter_by(id=dominio_id)
        obt_dominio = self.session.execute(stmt).one()
        return obt_dominio

    def remover(self, dominio_id: int):
        stmt = delete(models.Dominio).where(models.Dominio.id == dominio_id)
        
        self.session.execute(stmt)
        self.session.commit()
        #self.session.refresh(del_dominio)
        