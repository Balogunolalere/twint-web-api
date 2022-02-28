from fastapi import APIRouter
from models.user_model import *
from services.user_services import *

router = APIRouter()


@router.get('/')
async def search_username(user : User):
    resp = search_user(**user)
    return resp

@router.get('/profile/')
async def get_user_profile(profile: UserProfile):
    resp = get_profile(**profile)
    return resp

# @router.get('/{}/followers')
# async def get_user_followers():
#     return followers

# @router.get('/{}/following')
# async def get_following():
#     return following