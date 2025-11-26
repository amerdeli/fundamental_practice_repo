def convert_time():
# function converts entered amount of seconds to the format hours/minutes/seconds

    while True:
        try:
            input_time = int(input("Please enter time in seconds:"))
            if input_time < 0:
                raise Exception("Input needs to be a positive number!")
        except ValueError:
            print("Invalid input! Input needs to be a number!")
        except Exception as e:
            print(e)
        else:
            break


    calculated_hours = input_time // 3600
    #calculated_hours = int(input_time / 3600)

    #calculated_minutes = (input_time - (calculated_hours * 3600)) // 60     
    #calculated_minutes = int((input_time - (calculated_hours * 3600)) / 60) # same as line above
    calculated_minutes = (input_time % 3600) // 60                         # same as above
    
    #calculated_seconds = input_time - (calculated_hours * 3600) - (calculated_minutes * 60)
    calculated_seconds = (input_time % 3600) % 60 

    print(f"Your input corresponds to {calculated_hours} hours, {calculated_minutes} minutes "
          f"and {calculated_seconds} seconds.")

convert_time()
