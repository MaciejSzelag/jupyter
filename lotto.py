import random
import os

range_start = 1
range_stop = 50
range_end = range_stop - 1
range_n = 6

def clear_console():
    """Czyści konsolę w zależności od systemu operacyjnego"""
    os.system('cls' if os.name == 'nt' else 'clear') 


def game():
    play_again = "y"
    while play_again.lower() == "y":
        # Randomly drawn numbers - sample() ensures numbers are unique
        random_numbers = random.sample(range(range_start, range_stop), range_n) 
        # Numbers chosen by the user
        numbers_input = input(f"Choose {range_n} numbers between {range_start} and {range_end} separated by spaces:\n") 
        # Converts elements from numbers (strings) to integers and creates a list
        numbers_to_int = [int(x) for x in numbers_input.split()] 
        # Display drawn random numbers
        print(f"Drawn numbers:\n{random_numbers}\n") 
        
        # Creates a list of "hit" numbers – i.e. numbers that are in both lists: numbers_int and random_numbers  
        hit_numbers = [n for n in numbers_to_int if n in random_numbers] 
        # Creates a list of numbers that are greater than the allowed range (range_end)
        number_too_big = [x for x in numbers_to_int if x > range_end]

        if number_too_big:
            print("One of the number is above 49")
        else:
            #print("wszystko jest ok")
            # Check the amount of entered numbers in the input
            if  len(numbers_to_int) > range_n:
                print(f"Too many numbers!\nYou entered {len(numbers_to_int) }, there should be {range_n}.")
            
            elif  len(numbers_to_int) < range_n:
                print(f"Too few numbers!\nYou entered {len(numbers_to_int) }, there should be {range_n}.")
        
            else:
                # print(f"Thank you! Your numbers:\n{numbers_input.replace(" ",",")}")
                # Creates a copy of the list random_numbers into a separate variable random_int
                random_int = random_numbers.copy()
                if hit_numbers == random_int:
                    print("you WON, you hit the same numbers :", hit_numbers)
                elif hit_numbers:
                    print(f"you just hit {len(hit_numbers)} no. -> ", hit_numbers)
                else:
                    print("unfortunately, you didn't hit anything")   

        play_again = input("Do you want play again?\n(y/n)\n")

        if play_again.lower() == "y":
           clear_console()

    print("Thanks for playing")

game()
