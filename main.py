#!/usr/bin/python3
from ics import Calendar, Event
import os


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

def add_classes(cal):
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
        if not tutor_bool:
            show_tut = input("Add Tutorial and lab(y)? Or just Lab(n)? [y/n/q]: ").lower()
            if show_tut.startswith("q"):
                continue
            show_bool = show_tut.startswith('y')

        

if __name__ == "__main__":
    c = Calendar()
    print("Welcome to Calare\n")
    print("This is a tool that will generate a timetable for your classes given classcodes and other info")
    print("This tool is designed for Tutors doing 1 hour tutorials followed by 2 hour labs")
    print("OR Assistant Tutors doing 2 hour Labs")
    print("If you have other needs, this will be open source if you'd like : ^)")
    
    name = input("Enter Name: ")
    course = input("Enter Course Code: ")
    offering = input("Enter Offering,  ie 20T3: ")
    c.events.add(create_event("test", "2020-10-09 12:30:00", "2020-10-09 12:45:30"))
    
   
            
        
    
    
    filename = name +'-' + course + '-calare-tutor-timetable.ics'
    if os.path.isfile('./' + filename):
        raise Exception("Looks like the file", filename, "already exists\nPlease delete/rename it")


    with open(filename, 'w') as output_file:
        output_file.writelines(c)    
