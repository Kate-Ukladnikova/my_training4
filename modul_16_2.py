# Домашнее задание по теме "Валидация данных".
# Цель: научится писать необходимую валидацию для вводимых
# данных при помощи классов Path и Annotated.
# Задача "Аннотация и валидация".

from fastapi import FastAPI, Path
from typing import Annotated

from fastapi.openapi.models import Example

app = FastAPI()

# после активации виртуального окружения (в терминале: myenv\\Scripts\\activate) переходим в папку директории проекта: cd Modul16
# python -m uvicorn modul_16_2:app

@app.get("/")
async def welcome() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def validaciya_1(user_id: int = Path(ge=1, le=100, description="Enter User ID", example=1)) -> str:
    return f"Вы вошли как пользователь № {user_id}."

@app.get("/user/{username}/{age}")
async def validaciya_2(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Ekaterina")],
                    age: int = Path(ge=18, le=120, description="Enter age", example=55)) -> str:
    return f"Информация о пользователе. Имя: '{username}', Возраст: '{age}'."

