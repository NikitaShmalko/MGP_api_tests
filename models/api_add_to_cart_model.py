from pydantic import BaseModel


class AddToCartData(BaseModel):
    item_id: int
    total: str
    discount: str
    discount_numeric: int
    discount_coupon: str
    count: int

class AddToCartResponse(BaseModel):
    status: str
    data: AddToCartData
