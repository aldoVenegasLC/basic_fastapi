from sqlModel import SQLModel, Field, Relationship
from typing import List


class RaceBase(SQLModel):
    name: str = Field(default=None, unique=True, index=True)


class Race(RaceBase, table=True):
    id: int = Field(default=None, primary_key=True)
    characters: List["Character"] = Relationship(back_populates="race")


class CharacterBase(SQLModel):
    name: str = Field(default=None, index=True, unique=True)
    weapon: str = Field(default=None)


class Character(CharacterBase, table=True):
    id: int = Field(default=None, primary_key=True)
    race_id: int = Field(default=None, foreign_key="race.id")
    race: Race = Relationship(backpopulates="characters")
