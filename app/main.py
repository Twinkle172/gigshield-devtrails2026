from fastapi import FastAPI
from app.routes import auth_routes, protected_routes

app = FastAPI(title="AI Parametric Insurance API")

app.include_router(auth_routes.router)
app.include_router(protected_routes.router)


@app.get("/")
def home():
    return {"message": "AI Parametric Insurance API running"}