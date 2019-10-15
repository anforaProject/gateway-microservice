import os

from fastapi import APIRouter
from v1.client import aio

router = APIRouter()

user_server = f"http://localhost:{os.environ.get('users_port')}"

@router.get("/accounts/{id}")
async def retrive_user(id):

    request = await aio.get(f'{user_server}/{id}')
    json = await request.json()

    return json
    

@router.get("/accounts/{id}/followers")
async def retrive_user_followers(id, limit:int=40):

    params = {'limit':limit}
    
    request = await aio.get(f'{user_server}/{id}/followers',
                            params = params)
    json = await request.json()

    return json

@router.get("/accounts/{id}/following")
async def retrive_user_following(id, limit:int=40):

    params = {'limit':limit}

    request = await aio.get(f'{user_server}/{id}/following',
                            params = params)
    json = await request.json()

    return json

@router.get("/accounts/{id}/statuses")
async def retrive_user_statuses(id, limit:int=40):

    params = {'limit':limit}

    request = await aio.get(f'{user_server}/{id}/statuses',
                            params = params)
    json = await request.json()

    return json
