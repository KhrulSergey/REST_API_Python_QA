#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import locale
import calendar
import pytils

locale.setlocale(locale.LC_ALL, 'russian_russia')

from enum import Enum

class DayOfWeek(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6


# Date of schedule search
DepartureDate = datetime.date(2018, 4, 14)

# Format of viewing date
DateFormat = '%Y-%m-%d'

# Start date of departure (schedule search)
DepartureDay = DayOfWeek.Saturday.value

# months_dic ={0:'Январь', 1:'Февраль', 2:'Tue',3:'Wed',4:'Thu',5:'Fri',6:'Sat'}


def get_next_weekday(startdate, weekday):
    """
    @startdate: given date, in format '2013-05-25'
    @weekday: week day as a integer, between 0 (Monday) to 6 (Sunday)
    """
    t = datetime.timedelta((7 + weekday - startdate.weekday()) % 7)
    return startdate + t


if __name__ == '__main__':
    DepartureDate = get_next_weekday(datetime.date.today(), DepartureDay)
    print(DepartureDate)

    string_answer = pytils.dt.ru_strftime(u"%d %B, %A", date=DepartureDate, inflected=True)
    print(string_answer)
