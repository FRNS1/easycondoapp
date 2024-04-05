from datetime import datetime
from typing import Optional

class Payments(object):
    payment_id: Optional[int]
    booking: int
    price_cents: int
    status: str
    payment_date: datetime
    payment_method: str
    created_at: datetime
    created_by: int

    def __init__(
            self,
            booking: int,
            price_cents: int,
            status: str,
            payment_date: datetime,
            payment_method: str,
            created_at: datetime,
            created_by: int
    ):
        self.booking = booking
        self.price_cents = price_cents
        self.status = status
        self.payment_date = payment_date
        self.payment_method = payment_method
        self.created_at = created_at
        self.created_by = created_by

    def is_Valid(Self):
        return True