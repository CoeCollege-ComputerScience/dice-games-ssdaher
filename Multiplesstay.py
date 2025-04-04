import random 

def multiplesstay():
    dice_count = 10
    current_player = 0

    while dice_count > 0:
        print(f"Player {current_player + 1}'s turn with {dice_count} dice remaining.")
        rolls = [random.randint(1, 6) for _ in range(dice_count)]
        print(f"Rolls: {rolls}")

       
        counts = [rolls.count(i) for i in range(1, 7)]
        multiples = [(i + 1) for i, count in enumerate(counts) if count > 1]

        if not multiples:
            print(f"player {current_player +1} not able to remove multiples. Game over!")
            print(f"player { current_player} wins!")
            return

        print(f"Multiples available: {multiples}")
        choice = int(input(f" player {current_player + 1}choose a number to remove multiples of: {multiples}: "))
        while choice not in multiples:
            choice = int(input("Invalid choice. Choose a valid number: "))

        dice_count -= counts[choice - 1]
        print(f"Removed {counts[choice - 1]} dice showing {choice}. {dice_count} dice remain.")
        current_player = 1 - current_player

    print(f"All dice removed.{1 - current_player} wins!")
multiplesstay()