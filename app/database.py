import os
from typing import Any

from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv(find_dotenv())

engine = create_engine(os.getenv("DB_ENGINE"))
base = declarative_base()
base.metadata.create_all(engine)
session = sessionmaker(bind=engine)


@as_declarative()
class Base:
    id: Any
