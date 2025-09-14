import random 

name = input("What is your name?\n")
number_range_start = 1
number_range_end = 49
number_range = 6

def start_game():
    play_again = "y"
    while play_again.lower() == "y":    
        random_numbers = [random.randint(number_range_start, number_range_end) for _ in range(number_range)] # wybiera losowe numery midzy 1 a 49, petla w zakresie 6 w  tablicy

        # Zabezpieczenie przed błędnymi danymi
        try:
            y_number = int(input(f"{name} choose a random number between {number_range_start} a {number_range_end}\n"))
        except ValueError:
            print("Please enter valid number")
            continue

        # Sprawdź czy liczba jest w zakresie 1-49
        if y_number < number_range_start or y_number > number_range_end:
            print(f"Your number is {y_number}. Please choose a number between {number_range_start} and {number_range_end}\nTry again")
       
        elif y_number in random_numbers:
            print(f"{name}, you won!\nNumbers are {random_numbers} and your number is {y_number}.")
        else:   
            print(f"{name}, you lost: your number is {y_number}.\nNumbers are {random_numbers}.")    

        play_again = input(f"{name}, do you want play again?\n(y/n)\n")

    print(f"{name} thanks for playing")

start_game()