from fastapi import APIRouter, Depends, HTTPException, Header
from .pipeline import run_pipeline
from .auth import verify_token
from fastapi import APIRouter
from app.services.trigger import check_rain_trigger, check_no_orders
from app.services.weather import get_rainfall

router = APIRouter()

@router.get("/")
def home():
    return {"message": "API working"}

@router.get("/trigger/rain")
def rain_trigger(city: str):
    rainfall = get_rainfall(city)
    result = check_rain_trigger(rainfall)
    return {
        "city": city,
        "rainfall": rainfall,
        **result
    }

@router.get("/trigger/no-orders")
def no_orders(hours: int):
    result = check_no_orders(hours)
    return result
API_KEY = "supersecret"

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")
def get_current_user(authorization: str = Header(...)):
    token = authorization.split(" ")[1]
    return verify_token(token)

@router.post("/analyze", dependencies=[Depends(verify_api_key)])
async def analyze(data: dict):
    result = run_pipeline(data)
    return result