from datetime import datetime

from sqlalchemy import JSON, MetaData, Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# Создаем объект Engine для работы с базой данных
engine = create_engine('postgresql://postgres:@localhost/traiding_db', echo=True)

Base = declarative_base()

metadata = MetaData()


class Roles(Base):
    __tablename__ = 'roles'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    permissions = Column('permissions', JSON)


class Users(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    email = Column('email', String, nullable=False)
    username = Column('username', String, nullable=False)
    password = Column('password', String, nullable=False)
    registered_at = Column('registered_at', TIMESTAMP, default=datetime.utcnow)
    roles = relationship(Roles)

