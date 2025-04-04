import random

def rollDice():
    return random.randint(1,6) + random.randint(1,6)

def pig():
    player_scores = [0, 0]
    winning_score = 100
    current_player = 0

    while max(player_scores) < winning_score:
        print(f"Player {current_player + 1}'s turn")
        turn_total = 0

        while True:
            turn = input(f"Player {current_player + 1}, type 'roll' the dice...")
            if turn.lower() != 'roll':
                print("Invalid input, please type 'roll' to roll the dice.")
                continue
            roll = random.randint(1, 6)
            print(f"Player {current_player + 1} rolled: {roll}")
            if roll == 1:
                print("Rolled a 1! Turn over, no points added. ")
                turn_total = 0
                break #copilot suggested this to break the while loop 
            else:
                turn_total += roll
                print(f"Turn total: {turn_total}")
                choice = input("Hold or Roll again? (h/r): ").strip().lower()
                if choice == 'h':
                    print("Player holds.") 
                    break

        player_scores[current_player] += turn_total
        print(f"Player {current_player + 1}'s total score: {player_scores[current_player]}\n")

        if player_scores[current_player] >= winning_score:
            print(f"Player {current_player + 1} wins with a score of {player_scores[current_player]}!")
            break

        current_player = 1 - current_player
pig()