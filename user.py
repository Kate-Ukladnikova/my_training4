# Модель баз данных User:
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Null
from sqlalchemy.orm import relationship

from Modul_17.app.backend.db import Base
class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key = True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="user")

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))