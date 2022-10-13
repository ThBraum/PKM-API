from sqlalchemy.orm import Session
from server.schemas import schemas
from server.infra.sqlalchemy.models import models
from sqlalchemy import select, delete

class RepositorioDominio():
    def __init__(self, db: Session):
        self.db = db
    
    def criar(self, dominio: schemas.Dominio):
        db_dominio = models.Dominio(descricao=dominio.descricao, 
                                    valor=dominio.valor)
        self.db.add(db_dominio)
        self.db.commit()
        self.db.refresh(db_dominio)
        return db_dominio

    def listar(self):
        dominios = self.db.query(models.Dominio).all()
        return dominios

    def obter(self, dominio_id: int):
        stmt = select(models.Dominio).filter_by(id=dominio_id)
        obt_dominio = self.db.execute(stmt).one()
        return obt_dominio

    def remover(self, dominio_id: int):
        stmt = delete(models.Dominio).where(models.Dominio.id == dominio_id)
        
        self.db.execute(stmt)
        self.db.commit()
        #self.db.refresh(del_dominio)
        