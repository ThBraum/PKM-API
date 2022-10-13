from sqlalchemy import Column, Integer, Boolean, String
from server.infra.sqlalchemy.config.database import Base


class Dominio(Base): 
    __tablename__ = 'dominio'

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)
    valor = Column(Integer)