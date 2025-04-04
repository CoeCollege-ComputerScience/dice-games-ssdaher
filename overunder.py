import random 

def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

def OverUnder():
    player1_wins = 0
    player2_wins = 0

    while player1_wins < 6 and player2_wins < 6:
        print("New Round!")
        player1_roll = roll_dice()
        player1_total = sum(player1_roll)
        print(f"Player 1 rolled: {player1_roll} (Total: {player1_total})")

        guess = input("Player 2, guess 'Over' or 'Under': ").strip().lower()
        while guess not in ['over', 'under']:
            guess = input("Invalid input. Please guess 'Over' or 'Under': ").strip().lower()

        player2_roll = roll_dice()
        player2_total = sum(player2_roll)
        print(f"Player 2 rolled: {player2_roll} (Total: {player2_total})")

    
        if (guess == 'over' and player2_total > player1_total) or (guess == 'under' and player2_total < player1_total):
            print("Player 2 wins this round!")
            player2_wins += 1
        else:
            print("Player 1 wins this round!")
            player1_wins += 1

        print(f"Score: Player 1 - {player1_wins}, Player 2 - {player2_wins}\n")

        player1_wins, player2_wins = player2_wins, player1_wins

    if player1_wins == 6:
        print("Player 1 wins the match!")
    else:
        print("Player 2 wins the match!")

OverUnder()