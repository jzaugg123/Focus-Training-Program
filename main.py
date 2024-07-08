#Focus Program

'''The goal of this program is for the user to train their focus by keeping logs of how long they focus for, what their average focus time is for the week,
and being able to track progress for as long as applicable

The program has a few options

1. Start focus mode
    - This allows the user to start a timer in the background.
    - You may press a key to show the timer, or press a key to stop the studying altogether
    - This is saved in a .txt file on your computer for the other features
2. Progression
    - This allows the user to see how far they have come
    - 4 modes: Daily, Weekly, Monthly, All-Time
    - Daily: Shows performance for the day, including highest time spent studying, lowest, and average across the day
    - Weekly: Shows performance across the week, including highest, lowest, and average
    - Monthly: Shows performance across the month, including highest, lowest, and average
    - All-Time: Shows performance across your entirety of using the program, including highest, lowest, and average
3. End Program
    -Allows the user to end the program
     
The program uses the following modules:
Datetime: Allows to see how long you've studied, when the study session happened, and allows you to visualize data
pyinputplus: Allows for simple input validation
time: allows the program to take certain pauses so it can clearly display data to the user'''

import datetime
import pyinputplus as pyip
import time

def start_program():
    print("Welcome to the focus program!")
    time.sleep(1)
    print("Please select an option below!")
    time.sleep(1)

def display_menu():
    options = ["Start Focus Mode","View Progression","End Program"]
    optionChosen = pyip.inputMenu(options,"", numbered=True)
    print(optionChosen)
    return optionChosen

def focus_mode():
    start_time = datetime.datetime.now()
    user_input = "\n"
    while user_input == "\n":
        user_input = input("You are now focusing! Type 't' and press enter to see your current time, or press any other key to end the session!")
        if user_input == "t":
            current_time = datetime.datetime.now()
            current_time_studied = current_time - start_time
            print("You have studied for: \n")
            print(current_time_studied.seconds // 3600, "hours")
            print((current_time_studied.seconds % 3600) // 60, "minutes")
            print((current_time_studied.seconds % 60), "seconds")
            user_input = "\n"
        else:
            end_time = datetime.datetime.now()
            end_time_studied = end_time - start_time
            print("You have studied for: \n")
            print(end_time_studied.seconds // 3600, "hours")
            print((end_time_studied.seconds % 3600) // 60, "minutes")
            print((end_time_studied.seconds % 60), "seconds")
            test_file = open("Study Session Tracker.txt","a")
            test_file.write("Does this work?")
            test_file.close()

start_program()

option_selected = ""
while option_selected != "End Program":
    option_selected = display_menu()

    if option_selected == "Start Focus Mode":
        focus_mode()
    elif option_selected == "View Progression":
        pass
