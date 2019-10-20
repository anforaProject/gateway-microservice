from datetime import datetime, timedelta
import os
from typing import Union, Dict

import jwt
from starlette.responses import JSONResponse

from v1.client import aio
from v1.auth.forms import Login

SECRET = os.environ.get('SECRET_ANFORA', 'keepthisverysecret')
algorithm = 'HS512'

user_server = f"http://localhost:{os.environ.get('users_port')}/api/v1"

def validate(token)->dict:
    jwt.decode(token, SECRET, algorithms=algorithm)

async def create_refresh_token():
    pass

async def logout_user():
    pass

async def create_toke(user: Login, client_id)->Union[str, bool]:

    # Chech that there are a client with this credential

    
    
    # Check that an user with the credential exists

    data = {
        'username': user.username,
        'password': user.password
    }

    user_request = await aio.get(f'{user_server}/users/validate_credentials')

    if user_request.status != 200:
        return False

    encode_data = user_request.json()

    # Create jwt token

    encode_data['exp'] = datetime.utcnow() + timedelta(hours=3)
    encode_data['iat'] = datetime.utcnow()

    return jwt.encode(user_request.json(), SECRET, algorithm=algorithm)
    
