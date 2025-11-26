import random

def guess_number():
    
    print(f"Let's play the guess the number game! But let us first define the limits for the number!")
    
    while True:
        try:
            range_min = int(input("Enter the lower limit:"))
        except ValueError:
            print("Incorrect input! Input needs to be a number.")
        else:
            break
        
    while True:
        try:
            range_max  = int(input("Enter the upper limit:"))
            if range_max <= range_min:
                raise Exception("This doesn't really make sense, does it? The upper limit needs to be greater than the lower limit!")
        except ValueError:
            print("Incorrect input! Input needs to be a number.")
        except Exception as e:
            print(e)
        else:
            break
    
    while True:
        try:
            flag_limit_tries = input("Should we make it more interesting? We could limit the number of your tries! Do you want to do that? [yes/no]:")
            if (flag_limit_tries != "yes") and (flag_limit_tries != "no"):
                raise Exception("Just yes or no answer!")
        except Exception as e:
            print(e)
        else:
            break
    
    if flag_limit_tries == "yes":
        while True:
            try:
                number_of_tries = int(input("Enter the number of tries:"))
            except ValueError:
                print("Incorrect input! Input needs to be a number.")
            else:
                break
    else:
        number_of_tries = 999999
    
    random_number  = random.randint(range_min, range_max)
    
    print("Ok, I picked a number!")
    
    while True:
        try:
            guessed_number = int(input("What is your first guess? Please enter the value:"))
        except ValueError:
            print("Incorrect input! Input needs to be a number.")
        else:
            break
    
    counter_tries = 1;   
    
    while guessed_number != random_number:
        print("Ups, you are wrong!")
        if flag_limit_tries == "yes":
            if counter_tries < number_of_tries:
                print(f"But you have {number_of_tries - counter_tries} more tries! Use it wisely!")
            else:
                print("Sorry you have no more tries! Game end.")
                break
        if guessed_number < random_number:
            print(f"The number you are looking for is greater than {guessed_number}!")
        elif guessed_number > random_number:
            print(f"The number you are looking for is lower than {guessed_number}!")
        while True:
            try:
                guessed_number = int(input("You can try again! Enter your next guess:"))
            except ValueError:
                print("Incorrect input! Input needs to be a number.")
            else:
                counter_tries += 1
                break
        if guessed_number == random_number:
            print("You got it! Good job!")

guess_number()
