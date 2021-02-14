# calare

## Introduction

Disclaimer - this is by no means a reflection of my coding abilities, it's a small tool that I spun up quickly, to work. Pls don't hire/fire me based on the quality of this code :(

## Introduction

A tool designed for UNSW Tutors who wish to create an ICS file with their teaching timetable :) 

## Assumptions

Calare works under the assumption that you teach a 1 hour tutorial, followed by a 2 hour lab. 

It also does not schedule classes for midsemester break (currently set to week 6).

To edit these assumptions, see [constants.py](https://github.com/MrSpanishPear/calare/blob/master/constants.py)

Additionally, this tool currently only works for offerings that are in the range:
```
 20T3 <= offering <= 21T3
```

It will be extended when 2022 term dates are availiable. 

## Usage

First, install the needed requirements with: 
```
pip3 install -r requirements.txt
```

Running the command

```
./calare
```

or 

```
python3 calare
```

will lead you through an interactive sequence of steps. 

You will initially be asked to provide
 * Your Name
 * Course you are teaching
 * Offering (ie 20T3)

Then, you will infinitely be asked to add classes, and you will be prompted for: 
 * Class Code (ie H13A)
 * Tutor or Assistant Tutor? 
 * Do you want the tutorial to be added if you are an assistant tutor? 

Finally, the ICS file will be created for you to input into your Outlook or GCal :) 

Enjoy!

## Notes

Daylight savings bug fixed in [5da477c](https://github.com/MrSpanishPear/calare/commit/60c802b3bd11f46641df73a867b2b5f18255fba7)

Pretty fragile, but hopefully you can modify it to suit your needs! If you have any troubles, please tweet me @SpanishPear :D


## Future Features
 - [ ] Ability to parse the tutor timetable page, ie [1511](http://www.cse.unsw.edu.au/~give/Admindata/21T1/COMP1511_timetable.html)
 - [ ] Ability to provide text file input, make it more unix'y
 - [ ] Web interface?? idk
