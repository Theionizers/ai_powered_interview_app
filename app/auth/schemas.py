from pydantic import Field,EmailStr,BaseModel


class UserRegistration(BaseModel):
    name:str=Field(...,min_length=2,max_length=10)
    email:EmailStr
    password:str=Field(...,min_length=8)