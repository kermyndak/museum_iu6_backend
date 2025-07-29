from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

@router.get("/")
def get_root():
    return "Qwerty"
