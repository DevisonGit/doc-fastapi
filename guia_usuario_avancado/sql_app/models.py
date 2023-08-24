from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    # informa o nome da tabela as ser usado por esse modelo
    __tablename__ = "users"

    # cria os atributos do modelo, cada atributo representa uma coluna na tabela
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean,  default=True)

    # define um relacionamento
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owned_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")
