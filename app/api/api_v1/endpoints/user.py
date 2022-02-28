from fastapi import APIRouter, Depends
from app.models.user_model import User, UserFollowers, UserFollowing, UserProfile
from app.services.user_services import *

router = APIRouter()


@router.get('/')
async def search_username(user: User = Depends()):
    resp = await search_user(*user)
    return resp

@router.get('/profile/')
async def get_user_profile(profile: UserProfile = Depends()):
    resp = await get_profile(*profile)
    return resp

# @router.get('/{}/followers')
# async def get_user_followers():
#     return followers

# @router.get('/{}/following')
# async def get_following():
#     return following