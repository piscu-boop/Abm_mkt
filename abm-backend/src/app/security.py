from typing import Optional
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException



'''
    Loging with:
        user: admin 
        passwd: passwd
'''

__USERNAME__ = "abmmarket"

__JWTDUMMY__ = f'jwtDummy_{__USERNAME__}'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def token_auth1(token: str=Depends(oauth2_scheme)):
    if not token:
        raise HTTPException(401, "Invalid token")
    if  token != __JWTDUMMY__:
        raise HTTPException(401, "Invalid token")

def fake_hash_password(password: str):
    return "#swdedfer2sas_" + password

abm_users_db = {
    "admin": {
        "username": __USERNAME__,
        "full_name": "ABM MArketing User",
        "email": "",
        "hashed_password": "#swdedfer2sas_passwd",
        "disabled": False,
    },
}

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str