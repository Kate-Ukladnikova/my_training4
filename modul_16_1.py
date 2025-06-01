# Домашнее задание по теме "Основы Fast Api и маршрутизация".
# Цель: научиться создавать базовую маршрутизацию для обработки данных
# в FastAPI.
# Задача "Начало пути".

from fastapi import FastAPI

app = FastAPI()

# cd Modul16
# python -m uvicorn modul_16_1:app

@app.get("/")
async def welcome() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_number(user_id: str) -> str:
    return f"Вы вошли как пользователь № {user_id}."

@app.get("/user")
async def user_fio(username: str = "Andrey", age = "60") -> dict:
    return {"Информация о пользователе. Имя": username, "Возраст": age}

