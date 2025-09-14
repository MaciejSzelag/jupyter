age_under_13 = 13
legal_age = 18

age_retirement = 65


name = input("Enter your name\n")



def age_checker():
    try_again = "y"
    while try_again.lower() =="y":
        try:
            user_age = int(input("Enter your age\n"))
        except ValueError:
            print("Your age must be a number. Please try again.\n")
            continue

        if user_age <= age_under_13:
            if user_age == 13:
                print(f"{name}, You are 13 and access has been denied")
            elif user_age < 13:
                print(f"{name}, You are under 13 and access has been denied")
        elif user_age < legal_age:
            print(f"{name}, you have to be {legal_age} to have access")
        elif user_age >= age_retirement and user_age <= 110:
            print(f"{name}, I think you're to old for this sh*t")
        elif user_age >= legal_age and user_age < age_retirement:
            print(f"{name}, welcome in our great community.")
        else:
            print(f"Propably you are dead")
        try:
            try_again = input("Do you want to try again?\n (y/n) \n")  
        except ValueError:
            print
    
    print("Thanks for comming. See you next time mate!")

age_checker()
