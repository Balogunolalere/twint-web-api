from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username: str
    user_id: Optional[str] = None
    retweets: Optional[bool] = None 
    limit: Optional[int] = None
    store_object: bool = True
    
class UserProfile(BaseModel):
    username: str
    user_id: Optional[str] = None
    user_full: bool = True
    store_object: bool = True
    
class UserFollowers(BaseModel):
    username: str
    user_id: Optional[str] = None
    user_full: bool = True
    store_object: bool = True
    resume: Optional[str] = None
    
class UserFollowing(BaseModel):
    username: str
    user_id: Optional[str] = None
    user_full: bool = True
    store_object: bool = True
    resume: Optional[str] = None