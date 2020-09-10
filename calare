#!/usr/bin/python3
import sys
import os
import time
from ics import Calendar, Event
from dateutil.rrule import rrule, WEEKLY
from constants import NUM_WEEKS, TUT_LENGTH, LAB_LENGTH, DAYS, START_DATES


def create_event(event_name, event_start, event_end):
    '''
        Create's an event
        @param event_name:str - Name of the event
        @param event_start:str - Time of the event start, "yyyy-mm-dd HH:MM:SS"
        @param event_end:str - Time of event end
    '''
    e = Event()
    e.name = event_name
    e.begin = event_start
    e.end = event_end
    return e

def add_classes(cal, offering_code, coursecode):
    '''
        Continuously adds classes to the ICS.
        Uses user input of ClassCode and other settings
    '''
    while input("Add a class? [y/n]: ").lower().startswith('y'):
        print("---- Adding Class ----")
        print("If you enter some wrong information, answer q to restart")
        class_code = input("Class code? Ie H13A: ")

        if class_code.lower().startswith("q"):
            continue

        tutor_input = input("T or AT? : ").lower()
        if tutor_input.startswith("q"):
            continue

        tutor_bool = tutor_input.startswith('t')
        show_tut = True

        if not tutor_bool:
            show_tut_input = input("Add Tutorial and lab(y)? Or just Lab(n)? [y/n/q]: ").lower()

            if show_tut_input.startswith("q"):
                continue

            show_tut = show_tut_input.startswith('y')

        year = offering_code[:2]
        term = offering_code[2:]
        start_date = START_DATES.get(year).get(term)


        tut_start = class_code[1:3]
        lab_start = str(int(tut_start) + TUT_LENGTH)
        lab_end = str(int(lab_start) + LAB_LENGTH)
        # generate the weeks

        date_rule = rrule(WEEKLY, dtstart=start_date, count=NUM_WEEKS, byweekday=(DAYS[class_code[0]]))
        for i, dt in enumerate(date_rule):
            # midsem break - no classes
            if i == 5:
                continue

            # add tutorial
            if show_tut:
                event_name = " ".join([course.upper(), class_code, "TUT"])
                print(event_name)
                start = dt.strftime("%Y-%m-%d")+ " " + tut_start+":00:00"
                end = dt.strftime("%Y-%m-%d") + " " + lab_start +":00:00"

                cal.events.add(create_event(event_name, start, end))

            # add lab
            event_name = " ".join([coursecode.upper(), class_code, "LAB"])
            start = dt.strftime("%Y-%m-%d") + " " + lab_start+":00:00"
            end = dt.strftime("%Y-%m-%d") + " " + lab_end+":00:00"
            cal.events.add(create_event(event_name, start, end))

def get_offering():
    ''''
        Gets the offering from the user, and valida
    '''
    offering_v = input("Enter Offering,  ie 20T3: ")

    # BASIC parsing because ceebs
    while START_DATES.get(offering_v[:2]).get(offering_v[2:]) is None:
        offering_v = input("Invalid Offering (not a 20/21 term) - try again: ")

    return offering_v

def print_intro():
    '''
        Prints the intro to the program
    '''
    print("Welcome to Calare\n")
    print("This is a tool that will generate an ICS cal for your classes given classcodes and other info")
    print("This tool is designed for Tutors doing 9 x  1 hour tutorials followed by 2 hour labs")
    print("OR Assistant Tutors doing 2 hour Labs")
    print("If you have other needs, this will be open source if you'd like : ^)")

if __name__ == "__main__":
    c = Calendar()
    print_intro()

    name = input("Enter Name: ")
    course = input("Enter Course Code: ")
    offering = get_offering()

    add_classes(c, offering, course)

    filename = '-'.join([name, course, str(int(time.time())), '-calare-tutor-timetable.ics'])
    if os.path.isfile('./' + filename):
        print("Looks like the file", filename, "already exists :(\nPlease delete/rename it")
        sys.exit(1)

    with open(filename, 'w') as output_file:
        output_file.writelines(c)
