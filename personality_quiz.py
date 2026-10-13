bb = 0
ny = 0
italy = 0
sweden = 0

print("\nWelcome! I am going to tell you what country/city you should visit next based on your answers to some questions.")
answer1=input("On vacation, would you rather explore or swim?\n").lower()
if answer1 == "swim":
    bb+=2
    italy+=1
elif answer1 == "explore":
    sweden+=2
    ny+=2
    italy+=1
answer2=input("Would you rather visit historical sites or more mainstream ones\n").lower()
if answer2 == "historical" or answer2 == "historical sites":
    italy+=1
    sweden+=1
elif answer2 == "mainstream" or answer2 == "mainstream ones":
    ny+=2
answer6=input("Do you like walking (for long periods like a hike or exploration)?\n").lower()
if answer6 == "yes":
    italy+=1
    sweden+=1
    ny+=1
elif answer6 == "no":
    bb+=1
answer3=input("What is your favorite season?\n").lower()
if answer3 == "summer":
    italy+=1
    bb+=1
elif answer3 == "fall" or answer3 == "autumn":
    ny+=1
elif answer3 == "winter":
    sweden+=1
answer4=input("Do you prefer A. nature or B. city or C. beach\n").lower()
if answer4 == "a":
    sweden+=2
    italy+=1
elif answer4 == "b":
    ny+=2
    italy+=1
elif answer4 == "c":
    bb+=2
    italy+=1
answer5=input("Do you want to travel A. near B. medium C. far\n").lower()
if answer5 == "a":
    ny+=1
elif answer5 == "b":
    italy+=1
    sweden+=1
elif answer5 == "c":
    bb+=1
#final points
print(f"You got {ny} NY, {italy} italy, {sweden} sweden, and {bb} bora bora")
#they got more ny points than any other place
if ny > sweden and ny > bb and ny > italy:
    print("You should visit New York!")
#they got more sweden points than any other place
if sweden > ny and sweden > bb and sweden > italy:
    print("You should visit Sweden!")
#they got more bora bora points than any other place
if bb > sweden and bb > ny and bb > italy:
    print("You should visit Bora Bora!")
#they got more italy points than any other place
if italy > sweden and italy > bb and italy > ny:
    print ("You should visit Italy!")