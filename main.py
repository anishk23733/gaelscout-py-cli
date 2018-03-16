#!/usr/bin/env python3

import time
from scouting import update
from compscout import rankings
time.sleep(0.1)
print("Entering GaelScout Portal... ")
time.sleep(0.5)
choice = ''
url = ''
spreadsheet=''

while choice != 'exit':
    choice = input('Gael-Scout: 5327B$ ')

    if choice.startswith("help") == True:
        print("Current commands:")
        print("update <robot-events-url>")
        print("rankings <vex-db> (if used after update, vexdb url is unnecessary)")
    elif choice.startswith("exit") == True:
        break
    elif choice.startswith("rankings") == True:
        choice = choice.split(" ")
        if len(choice) == 1:
            rankings()
        elif len(choice) == 2:
            url = choice[1]
            rankings(url)
    elif choice.startswith("update") == True:
        choice = choice.split(" ")
        if len(choice) == 1:
            with open('data/urls.txt', 'r') as filehandle:
                url = filehandle.read()
                update(url)
        elif len(choice) == 2:
            if choice[1].startswith("http://") == True or choice[1].startswith("https://") == True or choice[1].startswith("www.") == True:
                url = choice[1]
                update(url)
            else:
                print("Invalid url.")
                pass
        else:
            print("Invalid dimensions.")
            print("Try 'update --help' for more information.")
    # elif choice.startswith("search") == True:
    #     choice = choice.split(" ")
    #     choice.remove("search")
    #     url = "https://www.robotevents.com/robot-competitions/vex-robotics-competition?seasonId=&eventType=&name="
    #     for word in choice:
    #         url += word + "+"
    else:
        print("bash: " + choice + ": command not found")
