place = input("You wake up. Where will ou go today?\n").lower()
if place == "la":
    print("It's sunny")
    choice1 = input("Would you like to go to Erewhon, The Grove, or the beach\n").lower()
    if choice1 == "erewhon":
        choice2 = input("Are you going to get a smoothie or sushi\n").lower()
        if choice2 == "smoothie":
            print("Yum!")
        if choice2 == "sushi":
            print("You get avocado")
        if choice1 == "the grove" or "grove":
            choice3 = input("What store do you want to go to?\n").lower()
            if choice3 == "Brandy":
                print("Maybe you'll meet Embreigh and Preslee")
        else: 
            print("Good choice!")
    if choice1 == "beach" or "the beach":
        print("Ooh! The waves look really good")
        choice4 = input("Do you want to go surfing or tan?").lower()
        if choice4 == "surfing":
            print("You ride some amazing waves!")
        if choice4 == "tan":
            ("You get a major tan")
if place == "Seattle":
    print("It is raining")
