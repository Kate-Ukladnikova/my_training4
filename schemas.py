# Создаю 4 схемы, наследуемые от BaseModel,
# для удобной работы с будущими объектами БД:

from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int
class CreateTask(BaseModel):
    title: str
    content: str
    priority: int
class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int