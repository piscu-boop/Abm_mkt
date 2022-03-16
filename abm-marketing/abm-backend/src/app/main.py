from fastapi import Depends, FastAPI, HTTPException, status

import app.db
from .db import Base, engine
from app.tables import *
from app.router import *
from app.security import *

app = FastAPI()

''' DB table Builder'''
Base.metadata.create_all(bind=engine) 



app.include_router(routerCompany)
app.include_router(routerBayer)
app.include_router(routerServprod)
app.include_router(routerIndustry)
app.include_router(routerCampaign)
app.include_router(routerKPI)
app.include_router(routerCamp_KPI)
app.include_router(routerCampaign_goals)
app.include_router(routerCamp_cont)

'''Security '''
__JWTDUMMY__ = 'jwtDummy_'
@app.post("/auth/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = abm_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": f'{__JWTDUMMY__}{user.username}', "token_type": "bearer"}
