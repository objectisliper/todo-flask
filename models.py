from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from utils import session_scope

Base = declarative_base()


class Note(Base):
    __tablename__ = 'Note'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
