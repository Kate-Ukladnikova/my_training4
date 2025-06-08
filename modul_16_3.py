# Домашнее задание по теме "CRUD Запросы: Get, Post, Put
# Delete."
# Цель: выработать навык работы с CRUD запросами.
# Задача "Имитация работы с БД":
# Создайте новое приложение FastAPI и сделайте CRUD запросы.
# Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}

from fastapi import FastAPI, Path
from typing import Annotated

# from pygame_example.main import current_size

app = FastAPI()

# после активации виртуального окружения (в терминале: myenv\\Scripts\\activate) переходим в папку директории проекта: cd Modul16
# python -m uvicorn modul_16_3:app

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_all_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def add_user(username: str, age=int) -> str:
    user_id = str(int(max(users, key=int)) +1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered."

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age=int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered."

@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f"User with {user_id} was deleted."
