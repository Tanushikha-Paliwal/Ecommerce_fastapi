from pydantic import BaseModel

class user(BaseModel):
    shop_name : str
    email : str
    phone : int
    password : str
    gst_no : int
