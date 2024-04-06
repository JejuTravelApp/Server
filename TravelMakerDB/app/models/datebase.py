from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "" # aws주소 올곳

#SQLALCHEMY engine생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#DB세션
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

#Base
Base = declarative_base()
