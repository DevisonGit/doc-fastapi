from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# url de conexão do banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:///.sql_app.db"

# mecanismo do sqlalchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# cada instancia de sessionlocal será uma sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# retorna uma classe para criar os modelos ORM
Base = declarative_base()
