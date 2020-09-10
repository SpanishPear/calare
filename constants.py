''''
    Constants used to inform Calare's date picker
'''

from datetime import date
from dateutil.rrule import  MO, TU, WE, TH, FR

NUM_WEEKS = 10
MIDSEMWEEK = 6
TUT_LENGTH = 1
LAB_LENGTH = 2

DAYS = {
    "M" : MO,
    "T" : TU,
    "W" : WE,
    "H" : TH,
    "F" : FR
}

START_DATES = {
    "20" : {
        "T2": date(2020, 6, 1),
        "T3": date(2020, 9, 14)
    },
    "21" : {
        "T0": date(2021, 1, 4),
        "T1": date(2021, 2, 8),
        "T2": date(2021, 5, 31),
        "T3": date(2021, 9, 13)
    }
}
