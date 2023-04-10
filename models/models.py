from datetime import datetime

from sqlalchemy import JSON, Boolean, MetaData, Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://postgres:@localhost/traiding_db', echo=True)
Base = declarative_base()
metadata = MetaData()

class Role(Base):
    __tablename__ = 'role'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    permissions = Column('permissions', JSON)


class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    email = Column('email', String, nullable=False)
    username = Column('username', String, nullable=False)
    password = Column('hashed_password', String, nullable=False)
    registered_at = Column('registered_at', TIMESTAMP, default=datetime.utcnow)
    role = Column('role', ForeignKey(Role.id))
    is_active = Column('is_active', Boolean, default=True, nullable=False)
    is_superuser = Column('is_superuser', Boolean, default=False, nullable=False)
    is_verified = Column('is_verified', Boolean, default=False, nullable=False)
