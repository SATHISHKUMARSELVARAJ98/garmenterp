from datetime import date
from app.common.enums import SeasonStatus

class SeasonEntity:
    def __init__(
        self,
        season_code: str,
        season_name: str,
        start_date: date | None,
        end_date: date | None,
        status: SeasonStatus
    ):
        self.season_code = season_code
        self.season_name = season_name
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
