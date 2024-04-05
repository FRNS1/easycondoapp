from datetime import datetime
from typing import Optional

class CondoAdmins(object):
    admin_id: Optional[int]
    user: int
    condo: int
    created_at: datetime
    created_by: int

    def __init__(
            self,
            user: int,
            condo: int,
            created_at: datetime,
            created_by: int,
    ):
        self.user = user
        self.condo = condo
        self.created_at = created_at
        self.created_by = created_by

    def is_Valid(Self):
        return True