import os

from fastapi import APIRouter, File, UploadFile
from client import aio

router = APIRouter()

media_server = f"http://localhost:{os.environ.get('media_port')}"

@router.get("/media/{id}")
async def retrive_user(id, file:UploadFile=File(...), description:str='', focus:str='0,0'):

    data = {
        'file':file,
        'description':description,
        'focus':focus
    }
    
    request = await aio.post(f'{media_server}/media', data=data)
    json = await request.text()

    return json
    
