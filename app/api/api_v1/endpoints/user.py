from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def search_username():
    return username

@router.get('/profile/')
async def get_user_profile():
    return profile

@router.get('/{}/followers')
async def get_user_followers():
    return followers

@router.get('/{}/following')
async def get_following():
    return following