from decouple import config


class Status():
    def __init__(self):
        self.name_system = config('NAME_SYSTEM')
        self.version = config('VERSION')
        self.developer = config('DEVELOPER')
        self.email = config('EMAIL')

    def to_JSON(self):
        return {
            'nameSystem': self.name_system,
            'version': self.version,
            'developer': self.developer,
            'email': self.email,
        }
