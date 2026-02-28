from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

#! carregando variáveis do .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL") #* string de conexaõ

engine = create_engine(DATABASE_URL) #* criando a conexão com o postgres

#! responsavel por criar sessões que vão conversaar com o banco de dados
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()