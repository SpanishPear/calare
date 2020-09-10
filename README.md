# calare


## Introduction

Calare is a Tool designed for UNSW Tutors who are looking for a way to export their teaching timetable to an ICS file.

It works under the assumption that you teach a 1 hour tutorial, followed by a 2 hour lab. 
It also does not schedule classes for midsemester break (week 6).

Additionally, this tool currently only works for offerings that are in the range:
```
 20T3<= offering <= 21T3
```

It will be extended when 2022 term dates are availiable. 

## Usage

First, install the needed requirements with: 
```
pip3 -r requirements.txt
```

Running the command

```
./calare
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
  
