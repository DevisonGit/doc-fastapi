from sqlalchemy import create_engine  # é usada para criar um mecanismo de conexão com o banco
from sqlalchemy.ext.declarative import declarative_base  # usado para criar classes e modelos declarativos
from sqlalchemy.orm import sessionmaker  # usada para criar sessões do banco de dados

# URL do banco
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Criando o mecanismo de conexão com o banco de dados usando a URL
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# representa uma sessão do banco de dados para executer operações
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base para definir modelos que representam as tabelas do banco de dados
Base = declarative_base()
