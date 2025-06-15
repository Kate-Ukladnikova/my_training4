# Домашнее задание по теме "Модели данных Pydantic"
# Цель: научиться описывать и использовать Pydantic модель.
# Задача "Модель пользователя"

from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

# после активации виртуального окружения (в терминале: myenv\\Scripts\\activate) переходим в папку директории проекта: cd Modul16
# python -m uvicorn modul_16_4:app

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int


# Инфо о пользователях
@app.get("/users")
async def get_all_users() -> List[User]:
    return users

# Добавление пользователя в базу данных
@app.post("/user/{username}/{age}")
async def add_user(username: Annotated[str, Path(min_length=2, max_length=20, description="Введите Ваше имя",
                                                 example="Edison")], age: Annotated[int, Path(ge=18, le=120,
                                                 description="Введите ваш возраст", example="25")]) -> User:
    try:
        user_id = (users[-1].id + 1) if len(users)>0 else 1
        user = User(id=user_id, username=username, age=age)
        users.append(user)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")

# Обновление данных пользователя
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: Annotated[str, Path(min_length=2, max_length=20, description="Введите Ваше имя",
                                                 example="Edison")], age: Annotated[int, Path(ge=18, le=120,
                                                 description="Введите ваш возраст", example="25")]) -> User:
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')

# Удаление пользователя по id
@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id-1)
        return f'Данные пользователя № {user_id} удалены.'
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')