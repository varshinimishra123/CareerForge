from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User
from app.core.security import verify_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    payload = verify_token(token)

    user_id = payload.get("user_id")

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user