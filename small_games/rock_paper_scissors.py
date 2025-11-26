import random

def rock_paper_scissors():
    
    options_list = ["rock", "paper", "scissors"]
    print("Lets play rock/paper/scisssors game! Do you want to play best of 3 or best of 5 game?")
    while True:
        try:
            number_of_games = int(input("Enter your choice (3/5):"))
            if number_of_games not in [3,5]:
                raise Exception("Invalid input! Input must be 3 or 5!")
        except ValueError:
            print("Invalid input! Input must be a number!")
        except Exception as e:
            print(e)
        else:
            break
    
    print(f"Best of {number_of_games} it is! Lets play!")
    
    player_wins = 0
    computer_wins = 0
    game_cnt = 1
    
    while True:
        print(f"------------- Game {game_cnt} -------------")    
        while True:
            players_choice = input("Enter your choice (rock/paper/scissors):").lower()
            if players_choice not in options_list:
                print("Invalid input!")
            else:
                break
    
        computers_choice = random.choice(options_list)
    
        print(f"Computers choice: {computers_choice}")
    
        if players_choice == "rock":
            if computers_choice == "scissors":
                winner = "Player"
                player_wins += 1
            elif computers_choice == "paper":
                winner = "Computer"
                computer_wins += 1
            else:
                winner = "Nobody"
        elif players_choice == "paper":
            if computers_choice == "rock":
                winner = "Player"
                player_wins += 1
            elif computers_choice == "scissors":
                winner = "Computer"
                computer_wins += 1
            else:
                winner = "Nobody"
        elif players_choice == "scissors":
            if computers_choice == "paper":
                winner = "Player"
                player_wins += 1
            elif computers_choice == "rock":
                winner = "Computer"
                computer_wins += 1
            else:
                winner = "Nobody"
                

        if winner == "Player" or winner == "Computer":
            print(f"{winner} won!")
            print(f"-------------------------------------------")
            game_cnt += 1
        else:
            print(f"{winner} won! Let us repeat this game!")
        
        if number_of_games == 3:     
            if player_wins >= 2:
                print("Congratulations! You won the series!")
                print(f"End result: Player {player_wins} - {computer_wins} Computer ")
                break
            elif computer_wins >= 2:
                print("Sorry! Computer won the series!")
                print(f"End result: Player {player_wins} - {computer_wins} Computer ")
                break
            else:
                print(f"Current result: Player {player_wins} - {computer_wins} Computer")
        elif number_of_games == 5:     
            if player_wins >= 3:
                print("Congratulations! You won the series!")
                print(f"End result: Player {player_wins} - {computer_wins} Computer ")
                break
            elif computer_wins >= 3:
                print("Sorry! Computer won the series!")
                print(f"End result: Player {player_wins} - {computer_wins} Computer ")
                break
            else:
                print(f"Current result: Player {player_wins} - {computer_wins} Computer")
    
    
# Start the game
rock_paper_scissors()
