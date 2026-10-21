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
homework=input("Before we get started, do you have any more homework you got today?\n")
if homework == "no":
    homework == "nothing"
for i in range(10):
    answer1=input("Would you like to view your grades, see your homework, plan you week, or notes?\n").lower()
    if answer1 == "grades":
        if grades == "A":
            print(f"You have all {grades}'s")
        else: 
            print(f"Your grades are:\n{grades}")
        time.sleep(2)
        input("Press enter when you are ready to move on")
    elif answer1 == "homework":
        if homework == "nothing":
            print(f"Your homework is {homework}. Good job!")
        else:
            print(f"Your homework is {homework}")
        time.sleep(2)
        input("Press enter when you are ready to move on")
    elif answer1 == "plan" or answer1 == "plan week" or answer1 == "plan my week":
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
            print(f"Your plan for the week is...\n{monday} on Monday\n{tuesday} on Tuesday\n{wednesday} on Wednesday\n{thursday} on Thursday\n{friday} on Friday\n{saturday} on Saturday\n{sunday} on Sunday\n")
            again=input("Would you like to plan another day?\n").lower()
            if again == "yes":
                time.sleep(1)
            elif again == "no":
                break
        input("Press enter when you want to move on")
    elif answer1 == "notes":
        notes=input("What would you like to write in your notes?\n")
        print(f"Your notes are {notes}")
        input("Press Enter when you want to move on")