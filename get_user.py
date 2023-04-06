from typing import Union

from fastapi import FastAPI


app = FastAPI(title="Traiding App")


fake_users = [
    {"id": 1, "name": "Nur", "number": 501332232},
    {"id": 2, "name": "Malika", "number": 501388588},
    {"id": 3, "name": "Samat", "number": 556330050}
]


@app.get("/user/{user_id}")
def get_user(user_id:int):
    return [user for user in fake_users if user.get('id') == user_id]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 100.00, "amount": 2.19},
    {"id": 2, "user_id": 2, "currency": "BTC", "side": "sell", "price": 50.00, "amount": 1.19},
]

@app.get("/trades")
def get_trade(limit: int, offset: int):
    return fake_trades[offset:][:limit]


fake_users2 = [
    {"id": 1, "name": "Nur", "number": 501332232},
    {"id": 2, "name": "Malika", "number": 501388588},
    {"id": 3, "name": "Samat", "number": 556330050}
]

@app.post("/change_name")
def change_name_user(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))[0] #Достаем пользователя по id
    current_user["name"] = new_name
    return {'status': 200, "data": current_user}

@app.patch("/user/{id}")
def change_number(id: int, new_number: int):
    for i in fake_users2:
        if i.get('id') == id:
            i['number'] = new_number
            return {'status': 200, "data": i}
    return {"status": 400, "data": "User not found"}

