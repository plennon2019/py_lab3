from pydantic import BaseModel, EmailStr, constr, conint

class Address(BaseModel):
    street: constr(min_length=3)
    number: int
    county: str
    country: str
    eircode: constr(min_length=7)