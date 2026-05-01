from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt

from app.core.config import settings
from app.core.database import SessionLocal


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/v1/login"
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


async def get_current_user(
    token: str = Depends(oauth2_scheme),
):

    try:

        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[
                settings.jwt_algorithm
            ],
        )

        username = payload.get("sub")

        if username is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token",
            )

        return username

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )