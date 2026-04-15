from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="CloudForge API")

app.include_router(router)

@app.get("/")
def home():
    return{"message": "CloudForge API running"}