from sqlalchemy.orm import Session
from server.schemas import schemas
from server.infra.sqlalchemy.models import models

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

    def obter(self):
        pass

    def remover(self):
        pass