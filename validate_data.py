from datetime import datetime
from enum import Enum

from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Traiding App")


fake_users = [
    {"id": 1, "name": "Nur", "number": 501332232},
    {"id": 2, "name": "Malika", "number": 501388588},
    {"id": 3, "name": "Samat", "number": 556330050, 
        "degree": [{"id": 1, "created_at": "2023-01-10T00:00:00", "degree": "expert"}]
    }
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 100.00, "amount": 2.19},
    {"id": 2, "user_id": 2, "currency": "BTC", "side": "sell", "price": 50.00, "amount": 1.19},
]


class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    degree: DegreeType


class User(BaseModel):
    id: int
    name: str
    number: int
    degree: Optional[List[Degree]] = []


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.get("/user/{user_id}", response_model=List[User])
def get_user(user_id:int):
    return [user for user in fake_users if user.get('id') == user_id]


@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}
