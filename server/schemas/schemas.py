from typing import Optional, List
from xmlrpc.client import boolean
from pydantic import BaseModel
from sqlalchemy import true
from server.infra.sqlalchemy.repositorios import *

class Dominio(BaseModel):
    id: Optional[int] = None
    descricao: str
    valor: int

    class Config:
        orm_mode = True

class Treinador(BaseModel):
    id: Optional[int] = None
    nome: str
    lider_ginasio: boolean = False
    descricao: str
    qt_insignias: int
    qt_pokemons: int

    class Config:
        orm_mode = True

class TreinadorSimples(BaseModel):
    id: Optional[int] = None
    nome: str

    class Config:
        orm_mode = True

class Pokemon(BaseModel):
    id: Optional[int] = None
    nome: str
    forma: int
    treinador: str
    tipo: str
    #treinador_id: int
    #owner: Optional[Treinador] #Treinador

    class Config:
        orm_mode = True
    