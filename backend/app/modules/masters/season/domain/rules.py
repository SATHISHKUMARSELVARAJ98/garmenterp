from app.common.enums import SeasonStatus

class SeasonRules:

    @staticmethod
    def ensure_can_modify(status: SeasonStatus):
        if status == SeasonStatus.CLOSED:
            raise ValueError("Closed season cannot be modified")

    @staticmethod
    def ensure_can_close(status: SeasonStatus):
        if status == SeasonStatus.CLOSED:
            raise ValueError("Season already closed")
