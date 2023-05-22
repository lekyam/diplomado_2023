status = {
    'NAME_SYSTEM': 'api_users',
    'VERSION': '0.0.1',
    'DEVELOPER': 'Josue Maykel Flores Rodriguez',
    'EMAIL': 'ullsaf3@gmail.com'
}


class Status():
    def __init__(self):
        self.name_system = status['NAME_SYSTEM']
        self.version = status['VERSION']
        self.developer = status['DEVELOPER']
        self.email = status['EMAIL']

    def to_JSON(self):
        return {
            'nameSystem': self.name_system,
            'version': self.version,
            'developer': self.developer,
            'email': self.email,
        }
