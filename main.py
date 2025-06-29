from fastapi import FastAPI

from routers import user
from routers import task

# создаем сущность FastAPI()
app = FastAPI()

# после активации виртуального окружения (в терминале: myenv\\Scripts\\activate) переходим в папку директории проекта: cd app
# python -m uvicorn main:app

# пишем для нее маршрут (функцию, которую обрабатывают HTTP-запросы)
@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)