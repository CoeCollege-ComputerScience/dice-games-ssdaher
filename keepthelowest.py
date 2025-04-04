import random 

def keepthelowest():
    player_scores = [0, 0]
    current_player = 0

    while all(score < 20 for score in player_scores):
        print(f"Player {current_player + 1}'s turn!")
        turn = input("Type 'roll' to roll the dice...")
        if turn.lower() != 'roll':
            print("Invalid input, please type 'roll' to roll the dice.")
            continue

        dice = [random.randint(1, 6) for _ in range(5)]
        kept = []
        while dice:
            print(f"Rolled dice: {dice}")
            lowest = min(dice)
            kept.append(lowest)
            print(f"Keeping the lowest die: {lowest}")
            dice.remove(lowest)
            if dice:
                turn2 = input("Type 'roll' to reroll the remaining dice...")
                if turn2.lower() != 'roll':
                    print("Invalid input, please type 'roll' to roll the dice.")
                    break
                dice = [random.randint(1, 6) for _ in range(len(dice))]
        print(f"Kept dice: {kept}")
        player_scores[current_player] += sum(kept)
        print(f"Player {current_player + 1}'s total score: {player_scores[current_player]}")

        if player_scores[current_player] >= 20:
            print(f"Player {current_player + 1} wins with a score of {player_scores[current_player]}!")
            break

        current_player = 1 - current_player  # Switch to the other player
keepthelowest()