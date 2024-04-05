from datetime import datetime
from typing import Optional

class AreasSpaces(object):
    space_id: Optional[int]
    space_type: int
    commom_area: int
    status: str
    created_at: datetime
    created_by: int

    def __init__(
            self,
            space_type: int,
            commom_area: int,
            status: str,
            created_at: datetime,
            created_by: int
    ):
        self.space_type = space_type
        self.commom_area = commom_area
        self.status = status
        self.created_at = created_at
        self.created_by = created_by

    def is_Valid(self):
        return True