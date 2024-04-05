from typing import Optional
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB

class Users(object):
    user_id: Optional[int]
    name: str
    username: str
    password: str
    password_created_at: datetime
    email: str
    phone: str
    created_at: datetime
    created_by: Optional[int]
    permissions: JSONB
    role: int
    condo: int
    apartment: str

    def __init__(
            self,
            name: str,
            username: str,
            password: str,
            password_created_at: datetime,
            email: str,
            phone: str,
            created_at: datetime,
            created_by: Optional[int],
            permissions: JSONB,
            role: int,
            condo: int,
            apartment: str
        ):
        self.name = name
        self.username = username
        self.password = password
        self.password_created_at = password_created_at
        self.email = email
        self.phone = phone
        self.created_at = created_at
        self.created_by = created_by
        self.permissions = permissions
        self.role = role
        self.condo = condo
        self.apartment = apartment

        def is_valid(self):
            return True
