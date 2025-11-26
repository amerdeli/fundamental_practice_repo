import random

def guess_word():
    
    
    print("Let's play the guess the word game! But let us first define some ground rules:")
    print("*) I will pick a word from a predefined list and you will try to guess it.")
    print("*) Number of attempts is then determined based on the word length.")
    print("*) You can guess the word by entering letters one by one,"
          "or you can try to guess the whole word at once.")
    print("*) If you want to guess the whole word, just enter it directly.")
    print("*) If you want to exit the game, just type 'exit'.\n")

    while True:
        try:
            use_txt_file = input("Do you want to use words from a specified .txt file? If no then "
                                 "an internal list of words will be used.[yes/no]:").lower()
            if use_txt_file != 'yes' and use_txt_file != 'no':
                raise Exception("Invalid input! Input must be 'yes' or 'no'.")
        except Exception as e:
            print(e)
        else:
            break
                
    if use_txt_file == 'yes':
        while True:
            try:
                txt_file_name = input("Enter the .txt file name:")
                words_file = open(txt_file_name, 'r')
            except IOError:
                print(f"{txt_file_name} doesn't exist in the current folder!")
            else:
                words = words_file.readlines()
                words = [word[:-1] for word in words]
                words_file.close()
                break
    else:
        words = ['mountain', 'river', 'ocean', 'forest', 'desert', 'castle', 'village', 'bridge', 
        'island', 'valley', 'garden', 'library', 'school', 'university', 'hospital', 
        'museum', 'stadium', 'theater', 'airport', 'station', 'market', 'restaurant', 
        'bakery', 'factory', 'office', 'computer', 'keyboard', 'monitor', 'printer', 
        'notebook', 'pencil', 'backpack', 'calendar', 'telephone', 'television', 
        'camera', 'bicycle', 'airplane', 'helicopter', 'submarine', 'rocket', 
        'planet', 'galaxy', 'universe', 'satellite', 'asteroid', 'comet', 'volcano', 
        'earthquake', 'tsunami', 'hurricane']
    
    word = random.choice(words).lower()
    word_len = len(word)
    number_attempts = word_len + int(word_len*0.5)
    guessed_letters = ['_'] * word_len
    
    print(f"I have picked the word! The word you are looking for has {word_len} characters and"
          f" you have {number_attempts} attempts.")
    
    letter_tries = []
    word_tries = []
    
    while number_attempts > 0:
        try:
            player_input = input("Enter your guess:").lower()
            if contains_number(player_input) or contains_special_char(player_input):
                raise Exception("Invalid input! Input contains at least one number or one special"
                                " character.")
        except Exception as e:
            print(e)
        else:
            if len(player_input) > 1:   # user entered a word
                if player_input not in word_tries:
                    if player_input == word:
                        print(f"Congrats, you guessed it right! {player_input} is correct!")
                        break
                    else:
                        print("Sorry, that is not the word you are looking for!")
                        number_attempts -= 1
                        if number_attempts == 0:
                            print("Sorry! You have no more attempts left. The word you were loking for "
                                  f"was {word}.")
                        else: 
                            print(f"You have {number_attempts} attempts left.")
                            word_tries.append(player_input)
                else:
                    print("You have already tried this! This attempt won't be counted.")            
            else:                      # user entered a single letter
                if player_input not in letter_tries:
                    for index, letter in enumerate(word):
                        if player_input == letter:
                            guessed_letters[index] = letter
                    print(' '.join(guessed_letters))
                    if '_' in guessed_letters:
                        number_attempts -= 1
                        if number_attempts == 0:
                            print("Sorry! You have no more attempts left. The word you were loking for "
                                f"was {word}.")
                        else: 
                            print(f"You have {number_attempts} attempts left.")
                            letter_tries.append(player_input)
                    else:
                        print(f"Congrats, you guessed it right! {word} is correct!")
                        break
                else:
                    print("You have already tried this! This attempt won't be counted.")              

# Define of some useful functions

def contains_number(input_str: str):
    # Function checks if the input argument contains a number
    
    numbers_char_list = [str(number) for number in range(0,10)]
    
    for character in input_str:
        if character in numbers_char_list:
            return True
            
    return False  


def contains_special_char(input_str: str):
    # Function checks if the input argument contains a special character
    
    special_chars = "^!§$%&/()=?´`-_.:,;+*#'\ß]}{[@€"
    
    for character in input_str:
        if character in special_chars:
            return True
            
    return False   




# start guess the word game
guess_word()
