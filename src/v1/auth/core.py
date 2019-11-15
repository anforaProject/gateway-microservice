from datetime import datetime, timedelta
import os
from typing import Union, Dict

from starlette.responses import JSONResponse
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import PyJWTError

from v1.client import aio
from v1.auth.forms import Login
from v1.auth.utils import create_access_token

SECRET = os.environ.get('SECRET_ANFORA', 'keepthisverysecret')
ALGORITHM = "HS512"

user_server = f"http://localhost:{os.environ.get('users_port')}/api/v1"

#user_request = await aio.get(f'{user_server}/users/validate_credentials')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")

async def authenticate_user(username:str, password:str) -> bool:

    user = await aio.get(f'{user_server}/accounts/verify_credentials')

    request_status = user.status

    if user.status >= 400:
        return False
    else:
        return json.load(await user.text())
    
    

async def get_current_user(token:str = Depends(oauth2_scheme))
    credentials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except PyJWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
