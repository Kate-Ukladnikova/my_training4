# Домашнее задание по теме "Шаблонизатор Jinja 2."
# Цель: научиться взаимодействовать с шаблонами Jinja 2 и
# использовать их в запросах.
# Задача "Список пользователей в шаблоне.

from fastapi import FastAPI, status, Body, Path, HTTPException, Request
from pydantic import BaseModel
from typing import List, Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

users = []

app = FastAPI()

# после активации виртуального окружения (в терминале: myenv\\Scripts\\activate) переходим в папку директории проекта: cd Modul16
# python -m uvicorn modul_16_5:app

class User(BaseModel):
    id: int = None
    username: str
    age: int

templates = Jinja2Templates(directory="templates")

# Инфо о пользователях
@app.get("/")
def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}")
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id-1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")

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