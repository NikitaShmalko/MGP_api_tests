from typing import Optional
from pydantic import BaseModel


class LoginData(BaseModel):
    redirect_url: str
    redirect_code: Optional[str]

class LoginResponse(BaseModel):
    status: str
    data: LoginData