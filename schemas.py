from pydantic import BaseModel, EmailStr, constr, conint
from another import Address

class User(BaseModel):
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    age: conint(gt=18)
    address: Address  # <--- NESTED!