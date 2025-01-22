# 2024/02/16 00:00|Домашнее задание по теме "Основы Fast Api и маршрутизация"

from fastapi import FastAPI

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def get_main_page():
    return "Главная страница"

@app.get("/user/admin")
async def get_admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def get_user_number(user_id: int):
    return f"Вы вошли как пользователь №  {user_id}"

@app.get("/user")
async def get_user_info(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)