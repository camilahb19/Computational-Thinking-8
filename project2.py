import time
def main():
    print("Welcome. It's the first day of school. You have 10 diamonds to spend and each choice you choose will cost a certain amount of diamonds.")
    time.sleep(4)
    print("REMEMBER: keep track of your diamonds.\n")
    time.sleep(3)
    diamonds = 10
    choice1 = input("Would you like to wake up or sleep in?\nWake up=0 diamonds\nSleep in=-2 diamonds\n").lower()
    if choice1 == "wake up":
        print("\nYou start your day and go down to eat breakfast")
    elif choice1 == "sleep in":
        diamonds-=2
        print("\nYou're running late and in a rush; but you go downstairs to eat breakfast")
        time.sleep(2)
        print(f"You have {diamonds} diamonds")
    else:
        print ("Pick a choice")
    time.sleep (2)
    choice2 = input("\nDo you eat nothing or croissant?\ncroissant=-2 diamonds\nnothing=0 diamonds\n").lower()
    if choice2 == "nothing":
        print ("\nYou are hungry")
    elif choice2 == "croissant":
        print("\nYou are filled")
        time.sleep(2)
        diamonds-=2
        print(f"You have {diamonds} diamonds")
    else:
        print ("Pick a choice")
    time.sleep(2)
    print("\nYou are about to leave for school")
    time.sleep(2)
    choice3 = input("\nDo you get driven to school, bus, or walk\nDrive=-3 diamonds\nBus=-1 diamond\nwalk=0 diamonds\n").lower()
    if choice3 == "drive" or choice3 == "drive to school" or choice3 == "driven to school":
        diamonds-=3
        print("\nYou get to school on time. +2 diamonds")
        time.sleep(2)
        diamonds+=2
        print(f"You have {diamonds} diamonds")
    elif choice3 == "bus":
        print("\nYou get there right as the bell rings")
        time.sleep(2)
        diamonds-=1
        print(f"You now have {diamonds} diamonds")
    elif choice3 == "walk":
        print("\nYou're late")
        time.sleep(2)
        print("You have to get a tardy slip---that'll cost a diamond")
        time.sleep(2)
        diamonds-=1
        print(f"You now have {diamonds} diamonds")
    else:
        print ("Pick a choice")
    print("\nYou're first class is Comp thinking")
    time.sleep(2)
    choice4 = input("\nDo you sit by your friends? Yes=-1 diamond. No=0 diamonds\n").lower()
    if choice4 == "yes":
        print("\nYou're not focusing. Josh gets mad and you don't finish your work")
        time.sleep(2)
        diamonds-=2 
        print(f"You now have {diamonds} diamonds")
    elif choice4 == "no":
        print("\nYou finish all your work")
        time.sleep(2)
        diamonds+=1
        print(f"You now have{diamonds} diamonds")
    else: 
        print("Pick a choice")
    time.sleep(2)
    print("\nYou see your crush in the hallway")
    choice5 = input("\nDo you talk to them, ignore them, or make eye contact. \nTalk=+3 \nIgnore:-4\nEye contact=-3\n").lower()
    if choice5 == "talk" or choice5 == "talk to them":
        choice6 = input("Do you choose to be nonchalant or say a pick up line").lower()
        if choice6 == "nonchalant" or choice6 == "be nonchalant":
            print("\nYou stutter and he walks away")
            time.sleep(2)
            diamonds-=5
            print(f"You now have {diamonds} diamonds")
            if diamonds<0:
                print("You used all your diamonds")
                print("You lose")   
                restart=input("Would you like to play again?\n").lower()
                if restart == "yes":
                    main()
                else:
                    exit()     
        elif choice6 == "pick up line" or choice6 == "say a pickup line":
            print("\nYou say your pick up line and it works. Score!")
            time.sleep(2)
            diamonds+=4
    elif choice5 == "ignore" or choice5 == "ignore them":
        diamonds-=3
        print(f"You now have {diamonds} diamonds remaining")
        if diamonds<0:
            print("You used all your diamonds")
            time.sleep()
            print("You lose")   
            time.sleep()
            restart=input("Would you like to play again?\n").lower()
            if restart == "yes":
                main()
            else:
                exit()     
    elif choice5 == "eye contact" or choice5 == "make eye contact":
        print("\nYou start blushing and get embarrassed")
        time.sleep(2)
        diamonds-=1
        print(f"You now have {diamonds} diamonds")
    else: 
        print("\nIt doesn't work and you and your crush don't interact")
    time.sleep(2)
    print("\nYou now go off for lunch\n")
    time.sleep(2)
    choice7 = input("Do you eat at Seoul Bowl or Starbucks or nothing.\nSeoul Bowl=2 diamonds\nStarbucks=2 diamonds\n").lower()
    if choice7 == "seoul bowl":
        print("\nThe line is super long")
        time.sleep(2)
        print("You were late getting back to campus and Josephs angry")
        time.sleep(2)
        diamonds-=4
        print(f"You now have {diamonds} diamonds")
        if diamonds<0:
            print("\nYou used all your diamonds")
            time.sleep(2)
            print("You lose")   
            restart=input("Would you like to play again?\n").lower()
            if restart == "yes":
                main()
            else:
                exit()   
    elif choice7 == "starbucks":
        print("\nYou get your drink but you have to run back to school")
        time.sleep(2)
        print("It was a close call")
        time.sleep(2)
        diamonds-=2
        print(f"You now have {diamonds} diamonds")
        if diamonds<0:
            print("You used all your diamonds")
            print("You lose")   
            restart=input("Would you like to play again?\n").lower()
            if restart == "yes":
                main()
            else:
                exit()       
    else:
        print("\nYou go hungry for the rest of the day and you now lose 3 diamonds")
        diamonds-=3
        print(f"You have {diamonds} diamonds")
    time.sleep(2)
    print("\nYour day is finally over")
    print("Hope you had a fun day at school!")
main()