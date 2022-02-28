from typing import Optional
import twint
import nest_asyncio

nest_asyncio.apply()

c = twint.Config()


def search_user(
    username:str,
    user_id: Optional[str],
    retweets: Optional[bool],
    limit: Optional[int],
    store_object: bool
) -> dict:
    
    if user_id:
        c.Username = username
        c.Store_object = store_object
        c.User_id = user_id
    elif retweets:
        c.Username = username
        c.Store_object = store_object
        c.Retweets = retweets
    elif limit:
        c.Username = username
        c.Store_object = store_object
        c.Limit = limit
    elif user_id and retweets:
        c.Username = username
        c.Store_object = store_object
        c.User_id = user_id
        c.Retweets = retweets
    elif user_id and limit:
        c.Username = username
        c.Store_object = store_object
        c.User_id = user_id
        c.Limit = limit
    elif retweets and limit:
        c.Username = username
        c.Store_object = store_object
        c.Retweets = retweets
        c.Limit = limit
    else:
        c.Username = username
        c.Store_object = store_object
        
    twint.run.Search(c)
    user = twint.output.users_list
    return user
        
def get_profile(
    username:str,
    user_id: Optional[str],
    user_full: bool,
    store_object: bool
) -> dict :
    
    if user_id:
        c.Username = username
        c.Store_object = store_object
        c.User_id = user_id
        c.User_full = user_full
    else:
        c.Username = username
        c.Store_object = store_object
        c.User_full = user_full    
        
    twint.run.Lookup(c)    
    user = twint.output.users_list[0]
    user.join_date
    return user
  
    
def get_user_followers(
    username:str,
    user_id: Optional[str],
    user_full: Optional[bool],
    resume: Optional[str],
    store_object: bool
) -> dict:
    
    if user_id:
        c.Username = username
        c.Store_object = store_object
        c.User_id = user_id
    elif resume:
        c.Username = username
        c.Store_object = store_object
        c.Resume = resume
    elif user_full:
        c.Username = username
        c.Store_object = store_object
        c.User_full = user_full
    elif user_id and resume:
        c.Username = username
        c.Store_object = store_object
        c.User_id = user_id
        c.Resume = resume
    elif user_id and user_full:
        c.Username = username
        c.Store_object = store_object
        c.User_id = user_id
        c.User_full = user_full
    elif resume and user_full:
        c.Username = username
        c.Store_object = store_object
        c.User_full = user_full
        c.Resume = resume
    else:
        c.Username = username
        c.Store_object = store_object
        
    twint.run.Search(c)
    user = twint.output.users_list
    return user

def get_user_following(
    username:str,
    user_id: Optional[str],
    user_full: Optional[bool],
    resume: Optional[str],
    store_object: bool
) -> dict:
    
    if user_id:
        c.Username = username
        c.Store_object = store_object
        c.User_id = user_id
    elif resume:
        c.Username = username
        c.Store_object = store_object
        c.Resume = resume
    elif user_full:
        c.Username = username
        c.Store_object = store_object
        c.User_full = user_full
    elif user_id and resume:
        c.Username = username
        c.Store_object = store_object
        c.User_id = user_id
        c.Resume = resume
    elif user_id and user_full:
        c.Username = username
        c.Store_object = store_object
        c.User_id = user_id
        c.User_full = user_full
    elif resume and user_full:
        c.Username = username
        c.Store_object = store_object
        c.User_full = user_full
        c.Resume = resume
    else:
        c.Username = username
        c.Store_object = store_object
        
    twint.run.Search(c)
    user = twint.output.users_list
    return user
    
    