from fastapi import APIRouter, Depends, HTTPException, Header
from .pipeline import run_pipeline
from .auth import verify_token
from app.services.trigger import check_rain_trigger, check_no_orders
from app.services.weather import get_rainfall

router = APIRouter()

API_KEY = "supersecret"

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return True

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")

    try:
        token = authorization.split(" ")[1]
    except:
        raise HTTPException(status_code=401, detail="Invalid token format")

    return verify_token(token)

@router.post("/analyze", dependencies=[Depends(verify_api_key)])
async def analyze(data: dict):
    result = run_pipeline(data)

    
    rainfall = get_rainfall(data.get("city", "unknown"))
    rain_trigger = check_rain_trigger(rainfall)

    no_order_trigger = check_no_orders(data.get("hours", 0))

    return {
        "pipeline_result": result,
        "rain_trigger": rain_trigger,
        "no_order_trigger": no_order_trigger
    }