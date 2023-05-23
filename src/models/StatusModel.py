from .entities.Status import Status


class StatusModel:
    @classmethod
    def get_status(self):
        status = Status()
        return status.to_JSON()
