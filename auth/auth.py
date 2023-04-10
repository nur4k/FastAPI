from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend


cookietransport = CookieTransport(cookie_max_age=3600)

SECRET = "SECRET"

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookietransport,
    get_strategy=get_jwt_strategy
)