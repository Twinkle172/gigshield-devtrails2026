# app/models.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    name: str
    city: str
    work_type: str
    password: str

class Plan(BaseModel):
    plan_name: str
    price: float
    coverage: str

class Policy(BaseModel):
    user_id: str
    plan_id: str
    start_date: datetime
    end_date: datetime
    status: str = "ACTIVE"

class Claim(BaseModel):
    user_id: str
    policy_id: Optional[str]
    amount: float
    reason: str
