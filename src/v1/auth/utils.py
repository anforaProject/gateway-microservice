from datetime import datetime, timedelta
from typing import Dict

import jwt
from passlib.context import CryptContext

from v1.client import aio

ALGORITHM = "HS512"


def create_access_token(data:Dict, exp_delta:timedelta=None):

    to_encode = data.copy()

    if exp_delta:
        expire = datetime.utcnow() + exp_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp':expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
    
