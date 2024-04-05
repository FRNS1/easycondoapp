from datetime import datetime
from typing import Optional

class AreasSpacesTypes(object):
    area_space_type_id: Optional[int]
    type: str
    created_at: datetime
    created_by: int

    def __init__(
            self,
            type: str,
            created_at: datetime,
            created_by: int
    ):
        self.type = type
        self.created_at = created_at
        self.created_by = created_by

    def is_Valid(self):
        return True