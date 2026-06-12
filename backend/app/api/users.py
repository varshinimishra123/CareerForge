from fastapi import APIRouter
from fastapi import Depends

from app.core.security import (
    oauth2_scheme,
    verify_token
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me")
def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    payload = verify_token(token)

    return {
        "email": payload.get("sub"),
        "user_id": payload.get("user_id")
    }