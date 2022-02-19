from re import A
from fastapi import APIRouter



router = APIRouter()

@router.get('/')
async def search_query():
    return query