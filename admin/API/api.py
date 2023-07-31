from  fastapi import APIRouter,Request,status,Depends,Form
from . models import *
from .pydentic import user
from fastapi.responses import JSONResponse,RedirectResponse,HTMLResponse
from fastapi_login import LoginManager
from fastapi.security import OAuth2PasswordRequestForm

app = APIRouter()
SECRET = 'your-secret-key'

@app.post('/')
async def registration(data:user):
    if await User.exists(phone=data.phone):
        return {"status":False , "message":"phone number already exists"}
    elif await user.exists(email=data.email):
        return {"status":False , "message": "email already exists"}
    else:
        user_obj = await user.create(shop_name=data.shop_name , email=data.email , phone=data.phone , password=data.password , gst_no=data.gst_no)
        return user_obj


@app.get('/all/')
async def all_data():
    user_obj = await user.all()
    return user_obj
