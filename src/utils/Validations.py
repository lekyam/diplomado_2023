from dateutil.parser import parse


class Validations():
    @classmethod
    def check_numbers(self, stringValue):
        try:
            int(stringValue)
            return True
        except ValueError:
            return False

    @classmethod
    def is_valid_date(self, date_string):
        try:
            parse(date_string)
            return True
        except ValueError:
            return False
