''''
    Constants used to inform Calare's date picker
'''

from datetime import date
from dateutil.rrule import MO, TU, WE, TH, FR

NUM_WEEKS = 10
MIDSEM_WEEK_NUMBER = 6
TUT_LENGTH_HOURS = 1
LAB_LENGTH_HOURS = 2


WEEKDAYS = {
    "MON": MO,
    "TUE": TU,
    "WED": WE,
    "THU": TH,
    "FRI": FR
}

CLASS_DAYS = {
    "M": MO,
    "T": TU,
    "W": WE,
    "H": TH,
    "F": FR
}

START_DATES = {
    "20": {
        "T2": date(2020, 6, 1),
        "T3": date(2020, 9, 14)
    },
    "21": {
        "T0": date(2021, 1, 4),
        "T1": date(2021, 2, 14), # sunday before W1
        "T2": date(2021, 5, 30),
        "T3": date(2021, 9, 12)
    }
}
