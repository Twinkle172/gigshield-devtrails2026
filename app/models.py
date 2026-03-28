# app/models.py
from pydantic import BaseModel

class User(BaseModel):
    name: str
    city: str
    work_type: str  # delivery, driver, etc.

class Plan(BaseModel):
    plan_name: str
    price: int
    coverage: str