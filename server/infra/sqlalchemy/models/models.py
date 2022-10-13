from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from server.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship, declarative_base


class Dominio(Base): 
    __tablename__ = 'dominio'

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)
    valor = Column(Integer)


class Treinador(Base):
    __tablename__ = 'treinador'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    lider_ginasio = Column(Boolean)
    descricao = Column(String)
    qt_insignias = Column(Integer)
    qt_pokemons = Column(Integer)

    pokemons = relationship('Pokemon', back_populates='owner')

class Pokemon(Base):
    __tablename__ = 'pokemon'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    forma = Column(Integer, ForeignKey('dominio.valor', name='fk_dominio.valor'))
    treinador = Column(String, ForeignKey('treinador.nome', name='fk_treinador.nome'))
    tipo = Column(String, ForeignKey('dominio.descricao', name='fk_dominio.descricao'))

    owner = relationship('Treinador', back_populates='pokemons')