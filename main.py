#!/usr/bin/python3
from O365 import Account, MSGraphProtocol
from credentials import credentials
import datetime as dt

if __name__ == "__main__":
    scopes = ['calendar_all', 'message_send', 'users'] #required permissions
    protocol = MSGraphProtocol(api_version="beta")
    account = Account(credentials, protocol=protocol)  
    if not account.is_authenticated:
        account.authenticate(scopes=scopes)

    schedule = account.schedule()
    calendar = schedule.get_default_calendar()
    new_event = calendar.new_event()
    new_event.subject = "TEST"
    new_event.location = "Basement"

    new_event.start = dt.datetime(2020, 9, 10, 12, 30)
    new_event.recurrence.set_daily(1, end=dt.datetime(2020, 9, 15))
    new_event.save()
