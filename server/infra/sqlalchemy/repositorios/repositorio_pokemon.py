from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from server.infra.sqlalchemy.models import models
from server.schemas import schemas
from sqlalchemy import select, delete, update


class RepositorioPokemon():
    def __init__(self, session: Session):
        self.session = session
    
    def criar(self, pokemon: schemas.Pokemon):
        session_pokemon = models.Pokemon(nome=pokemon.nome,
                                        forma=pokemon.forma,
                                        treinador=pokemon.treinador,
                                        tipo=pokemon.tipo)
        self.session.add(session_pokemon)
        self.session.commit()
        self.session.refresh(session_pokemon)
        return session_pokemon

    def listar(self):
        stmt = select(models.Pokemon)
        row = self.session.execute(stmt).scalars().all()
        return row

    def obter(self, pokemon_id: int):
        stmt = select(models.Pokemon).filter_by(id=pokemon_id)
        row = self.session.execute(stmt).scalars().one()
        return row

    def remover(self, pokemon_id: int):
        stmt = delete(models.Pokemon).where(models.Pokemon.id == pokemon_id)
        
        self.session.execute(stmt)
        self.session.commit()

    def editar(self, pokemon: schemas.Pokemon):
        stmt = update(models.Pokemon).where(
            models.Pokemon.id == pokemon.id
        ).values(nome=pokemon.nome,
                forma=pokemon.forma,
                treinador=pokemon.treinador,
                tipo=pokemon.tipo
        )
        self.session.execute(stmt)
        self.session.commit()
