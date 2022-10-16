from typing import Optional, List
from xmlrpc.client import boolean
from pydantic import BaseModel

class Dominio(BaseModel):
    id: Optional[str] = None
    descricao: str
    valor: int

    class Config:
        orm_mode = True

class Treinador(BaseModel):
    id: Optional[str] = None
    nome: str
    lider_ginasio: boolean = False
    descricao: Optional[str] = None
    qt_insignias: int
    qt_pokemons: int

    class Config:
        orm_mode = True

class Pokemon(BaseModel):
    id: Optional[str]
    nome: str
    #forma: int(Dominio.valor)
    #treinador: str(Treinador.nome)
    #tipo: str(Dominio.descricao)
    