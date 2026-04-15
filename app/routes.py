from fastapi import APIRouter
from app.services import create_env, stop_env, start_env, restart_env, destroy_env, get_status

router = APIRouter()

@router.post("/create-environment")
def create_environment():
    return create_env()

@router.post("/stop")
def stop():
    return stop_env()

@router.post("/start")
def start():
    return start_env()

@router.post("/restart")
def restart():
    return restart_env()

@router.delete("/destroy-environment")
def destroy_environment():
    return destroy_env()

@router.get("/status")
def status():
    return get_status()