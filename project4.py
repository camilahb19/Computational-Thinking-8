import time
grades = "A"
homework = "nothing"
monday = "nothing"
tuesday = "nothing"
wednesday = "nothing"
thursday = "nothing"
friday = "nothing"
saturday = "nothing"
sunday = "nothing"
notes = "nothing"
print("Hello! I am here to assist you and help you stay organized!")
homework=input("Before we get started, do you have any more homework you got today?\n").lower()
if homework == "no":
    homework = "nothing"
#loop for lines 18-77. Makes it loop back to line 18. 
for i in range(10):
    answer1=input("Would you like to view your grades, see your homework, plan you week, or notes?\n").lower()
    if answer1 == "grades":
        if grades == "A":
            print(f"You have all {grades}'s")
        else: 
            print(f"Your grades are:\n{grades}")
        time.sleep(2)
        first=input("Would you like to keep going?\n").lower()
        if first == "yes":
            input("Press Enter when you want to move on")
        elif first == "no":
            quit()
    elif answer1 == "homework" or answer1 == "see my homework" or answer1 == "see homework":
        if homework == "nothing":
            print(f"Your homework is {homework}. Good job!")
        else:
            print(f"Your homework is {homework}")
        time.sleep(2)
        second=input("Would you like to keep going?\n").lower()
        if second == "yes":
            input("Press Enter when you want to move on")
        elif second == "no":
            quit()
    elif answer1 == "plan" or answer1 == "plan week" or answer1 == "plan my week":
#double loop for lines 44-70. 
        for i in range(10):
            answer2=input("What day would you like to plan?\n").lower()
            if answer2 == "monday":
                monday=input("Type your plan below\n")
            elif answer2 == "tuesday":
                  tuesday=input("Type your plan below\n")
            elif answer2 == "wednesday":
                wednesday=input("Type your plan below\n")
            elif answer2 == "thursday":
                thursday=input("Type your plan below\n")
            elif answer2 == "friday":
                friday=input("Type your plan below\n")
            elif answer2 == "saturday":
                saturday=input("Type your plan below\n")
            elif answer2 == "sunday":
                sunday=input("Type your plan below\n")
            week=input("Are you done planning or no?\n").lower()
            if week == "yes" or week == "done planning":
                time.sleep(1)
                print(f"\nYour plan for the week is...\n{monday} on Monday\n{tuesday} on Tuesday\n{wednesday} on Wednesday\n{thursday} on Thursday\n{friday} on Friday\n{saturday} on Saturday\n{sunday} on Sunday\n")
                time.sleep(1)
                sixth=input("Would you like to quit the program or go back to the start?").lower
                if sixth == "quit" or sixth == "quit program" or sixth == "quit the program":
                    quit()
                elif sixth == "go back to start" or sixth == "start" or sixth == "back to start" or sixth == "back to the start":
                    break
            elif week == "no":
                time.sleep(0.1)
    elif answer1 == "notes":
        notes=input("What would you like to write in your notes?\n")
        print(f"Your notes are {notes}")
        fourth=input("Would you like to keep going?\n").lower()
        if fourth == "yes":
            input("Press enter when you want to move on")
        elif fourth == "no":
            quit()