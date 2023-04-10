from fastapi_users import fastapi_users, FastAPIUsers
from fastapi import Depends, FastAPI

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.shcemas import UserCreate, UserRead

app = FastAPI(title="Traiding App")


fastapi_users = FastAPIUsers[User, int](
    get_user_manager, 
    [auth_backend]
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"]
)


current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}! "


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonim! "
