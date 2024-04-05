from datetime import datetime
from typing import Optional

class CommomAreas(object):
    area_id: Optional[int]
    area_name: str
    area_type: int
    condo: int
    need_payment: bool
    price_Cents: int
    status: str
    created_at: datetime
    created_by: datetime
    
    def __init__(
            self,
            area_name: str,
            area_type: int,
            condo: int,
            need_payment: bool,
            price_Cents: int,
            status: str,
            created_at: datetime,
            created_by: datetime
    ):
        self.area_name = area_name
        self.area_type = area_type
        self.condo =  condo
        self.need_payment = need_payment
        self.price_Cents = price_Cents
        self.status = status
        self.created_at = created_at
        self.created_by = created_by

    def is_valid(self):
        return True