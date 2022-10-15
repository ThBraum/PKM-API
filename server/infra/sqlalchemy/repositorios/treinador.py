from distutils import text_file
from sqlalchemy.orm import Session
from server.infra.sqlalchemy.models import models
from server.schemas import schemas
from sqlalchemy import select, delete

class RepositorioTreinador():
    def __init__(self, session: Session):
        self.session = session

    def criar(self, treinador: schemas.Treinador):
        session_treinador = models.Treinador(nome=treinador.nome, 
                                            lider_ginasio=treinador.lider_ginasio,
                                            descricao=treinador.descricao)

        self.session.add(session_treinador)
        self.session.commit()
        self.session.refresh(session_treinador)
        return session_treinador

    def listar(self):
        treinador = self.session.query(models.Treinador).all()
        return treinador

    def obter(self, treinador_id: int):
        stmt = select(models.Treinador).filter_by(id=treinador_id)
        obt_treinador = self.session.execute(stmt).one()
        return obt_treinador

    def remover(self, treinador_id: int):
        stmt = delete(models.Treinador).where(models.Treinador.id == treinador_id)
        
        self.session.execute(stmt)
        self.session.commit()