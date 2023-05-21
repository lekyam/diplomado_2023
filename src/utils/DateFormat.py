import datetime


class DateFormat():

    @classmethod
    def conver_date(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')
