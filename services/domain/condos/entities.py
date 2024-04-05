from datetime import datetime
from typing import Optional

class Condos(object):
    condo_id: Optional[int]
    condo_name: str
    floors: int
    apartments: int
    towers: int
    houses_condo: bool
    houses: int
    address: str
    number: str
    neighbourhood: str
    city: str
    state: str
    country: str
    zip_code: str
    created_at: datetime
    created_by: int

    def __init__(
            self,
            condo_name: str,
            floors: int,
            apartments: int,
            towers: int,
            houses_condo: bool,
            houses: int,
            address: str,
            number: str,
            neighbourhood: str,
            city: str,
            state: str,
            country: str,
            zip_code: str,
            created_at: datetime,
            created_by: int
    ):
        self.condo_name = condo_name
        self.floors = floors
        self.apartments = apartments
        self.towers = towers
        self.houses_condo = houses_condo
        self.houses = houses
        self.address = address
        self.number = number
        self.neighbourhood = neighbourhood
        self.city = city
        self.state = state
        self.country = country
        self.zip_code = zip_code
        self.created_at = created_at
        self.created_by = created_by

    def is_Valid(Self):
        return True
