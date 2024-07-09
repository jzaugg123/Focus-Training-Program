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
time: allows the program to take certain pauses so it can clearly display data to the user
pip: installs pyinputplus and any other packages that you may need'''

import datetime
import pyinputplus as pyip
import time
import pip

if hasattr(pip,"main"):
    pip.main(['install','pyinputplus'])
else:
    pip._internal.main(['install','pyinputplus'])


def start_program():
    data_file = open("Study Session Tracker.txt","w")
    data_file.close()
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
            total_seconds = end_time_studied.seconds
            hours = end_time_studied.seconds // 3600
            minutes = (end_time_studied.seconds % 3600) // 60
            seconds = (end_time_studied.seconds % 60)
            print("You have studied for: \n")
            print(hours, "hours")
            print(minutes, "minutes")
            print(seconds, "seconds")
            test_file = open("Study Session Tracker.txt","a")
            test_file.write(f'[{total_seconds},{hours}, {minutes}, {seconds}, {start_time}, {end_time}]')
            test_file.close()

def see_progress():
    pass

def calculate_max(list_to_calc):
    pass

def calculate_average(list_to_calc):
    pass

def calculate_min(list_to_calc):
    pass

def convert_to_seconds(time):
    return (time[0] * 3600) + (time[1] * 60) + (time[2])

def convert_to_clocktime(time):
    hours = time // 3600
    minutes = (time % 3600) // 60
    seconds = time % 60

    return [hours,minutes,seconds]
    

start_program()

option_selected = ""
while option_selected != "End Program":
    option_selected = display_menu()

    if option_selected == "Start Focus Mode":
        focus_mode()
    elif option_selected == "View Progression":
        pass
