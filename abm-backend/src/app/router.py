
from fastapi import Depends, HTTPException
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from fastapi.security import OAuth2PasswordRequestForm

from app.db import Base, get_db
from app.security import (UserInDB, abm_users_db, fake_hash_password,
                          token_auth1)
from app.tables.bayerpersona import *
from app.tables.camp_kpi import *
from app.tables.campaign import *
from app.tables.company import *
from app.tables.industries import *
from app.tables.kpi import *
from app.tables.servprod import *
from app.tables.campaign_goals import *
from app.tables.camp_cont import *
from app.tables.cg_camp import *

''' Routers'''



'''         CRUD '''
routerCompany = SQLAlchemyCRUDRouter(
    schema=Company,
    create_schema=CompanyCreate,
    db_model=CompanyModel,
    dependencies=[Depends(token_auth1)],
    db=get_db,
    prefix='company'
)

routerBayer = SQLAlchemyCRUDRouter(
    schema=Bayerpersona,
    create_schema=BayerpersonaCreate,
    db_model=BayerpersonaModel,
    dependencies=[Depends(token_auth1)],
    db=get_db,
    prefix='bayerpersona'
)
routerIndustries = SQLAlchemyCRUDRouter(
    schema=Industries,
    create_schema=IndustriesCreate,
    db_model=IndustriesModel,
    dependencies=[Depends(token_auth1)],
    db=get_db,
    prefix='industry'
)
routerServprod = SQLAlchemyCRUDRouter(
    schema=Servprod,
    create_schema=ServprodCreate,
    db_model=ServprodModel,
    # dependencies=[Depends(token_auth)],
    db=get_db,
    prefix='servprod'
)
routerCampaign = SQLAlchemyCRUDRouter(
    schema=Campaign,
    create_schema=CampaignCreate,
    db_model=CampaignModel,
    dependencies=[Depends(token_auth1)],
    db=get_db,
    prefix='campaigns'
)
routerKPI = SQLAlchemyCRUDRouter(
    schema=KPI,
    create_schema=KPICreate,
    db_model=KPIModel,
    #dependencies=[Depends(token_auth)],
    db=get_db,
    prefix='kpi'
)
routerCamp_KPI = SQLAlchemyCRUDRouter(
    schema=Camp_KPI,
    create_schema=Camp_KPICreate,
    db_model=Camp_KPIModel,
    #dependencies=[Depends(token_auth)],
    db=get_db,
    prefix='camp_kpi'
)
routerCampaign_goals = SQLAlchemyCRUDRouter(
    schema = Campaign_goals,
    create_schema = Campaign_goalsCreate,
    db_model = Campaign_goals_Model,
    #dependencies=[Depends(token_auth)],
    db = get_db,
    prefix = "campaing_goals"
)
routerCamp_cont = SQLAlchemyCRUDRouter(
    schema = Camp_cont,
    create_schema = Camp_contCreate,
    db_model = Camp_cont_Model,
    #dependencies=[Depends(token_auth)],
    db = get_db,
    prefix = "camp_cont"
)
routerCg_camp = SQLAlchemyCRUDRouter(
    schema = Cg_camp,
    create_schema = Cg_campCreate,
    db_model = Cg_camp_Model,
    #dependencies=[Depends(token_auth)],
    db = get_db,
    prefix = "cg_camp"
)