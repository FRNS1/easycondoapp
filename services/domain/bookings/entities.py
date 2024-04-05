from datetime import datetime
from typing import Optional

class Bookings(object):
    booking_id: Optional[int]
    user: int
    commom_area: int
    check_in: datetime
    check_out: datetime
    status: str
    space: Optional[int]
    created_at: datetime
    created_by: int

    def __init__(
            self,
            user: int,
            commom_area: int,
            check_in: datetime,
            check_out: datetime,
            status: str,
            space: Optional[int],
            created_at: datetime,
            created_by: int
    ):
        self.user = user
        self.commom_area = commom_area
        self.check_in = check_in    
        self.check_out = check_out
        self.status = status
        self.space = space
        self.created_at = created_at
        self.created_by = created_by

    def is_valid(Self):
        return True