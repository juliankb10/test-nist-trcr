from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import (
    OAuth2PasswordRequestForm,
)

from app.core.security import (
    create_access_token,
)

router = APIRouter()

TMP_USER = {
    "username": "admin",
    "password": "admin123",
}

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
):

    if (
        form_data.username
        != TMP_USER["username"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    if (
        form_data.password
        != TMP_USER["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    access_token = create_access_token({
        "sub": form_data.username,
    })

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }