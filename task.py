# Модели баз данных:

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Null
from sqlalchemy.orm import relationship
from Modul_17.app.models import *

from Modul_17.app.backend.db import Base
class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key = True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default = 0)
    completed = Column(Boolean, default = False)
    # user_id - целое число, внешний ключ на id из таблицы 'users' (Внешний ключ к users.id),
    # не NULL, с индексом
    user_id = Column(Integer, ForeignKey('users.id'), nullable = not Null, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship("User", back_populates="tasks")

from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))

