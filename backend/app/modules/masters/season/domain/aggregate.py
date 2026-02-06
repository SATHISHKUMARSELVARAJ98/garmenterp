from app.modules.masters.season.domain.rules import SeasonRules
from app.common.enums import SeasonStatus

class SeasonAggregate:

    def __init__(self, entity):
        self.entity = entity

    def update_details(self, season_name=None, start_date=None, end_date=None):
        SeasonRules.ensure_can_modify(self.entity.status)

        if season_name is not None:
            self.entity.season_name = season_name
        if start_date is not None:
            self.entity.start_date = start_date
        if end_date is not None:
            self.entity.end_date = end_date

    def close_season(self):
        SeasonRules.ensure_can_close(self.entity.status)
        self.entity.status = SeasonStatus.CLOSED
