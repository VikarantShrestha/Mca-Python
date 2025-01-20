import random

total_sticks = 21

print("Welcome to the Matchstick Game!")

while total_sticks > 1:

    if total_sticks == 1:
        print("You were forced to pick the last matchstick. You lose!")
        break

    # Player's turn
    print(f"There are {total_sticks} matchsticks left.")
    player_pick = int(input("How many matchsticks do you want to pick (1-4)? "))

    if player_pick < 1 or player_pick > 4 or player_pick > total_sticks:
        print("Invalid pick. You can pick between 1 and 4 matchsticks.")
        continue

    total_sticks -= player_pick

    if total_sticks % 5 == 0:
        computer_pick = random.randint(1, 4)
    else:
        computer_pick = total_sticks % 5
        if computer_pick == 0:
            computer_pick = 1

    print(f"Computer picks {computer_pick} matchstick(s).")
    total_sticks -= computer_pick

    if total_sticks == 1:
        print("The computer was forced to pick the last matchstick. You win!")
        break

print("Game Over!")
