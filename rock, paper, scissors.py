import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0
rounds = 5

print("Welcome to Rock-Paper-Scissors (Best of 5)!")
print("Make your choice: rock, paper, or scissors.\n")

for round_num in range(1, rounds + 1):
    print(f"Round {round_num} of {rounds}")
    player = input("Enter rock, paper, or scissors: ").lower()
    
    if player not in choices:
        print("Invalid choice! You lose this round by default.\n")
        computer_score += 1
        continue
    
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    if player == computer:
        print("It's a tie!\n")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round!\n")
        player_score += 1
    else:
        print("You lose this round!\n")
        computer_score += 1
    
    print(f"Current Score -> You: {player_score} | Computer: {computer_score}\n")

# After all rounds
print("Final Results after 5 Rounds:")
print(f"You: {player_score} | Computer: {computer_score}")

if player_score > computer_score:
    print("Congratulations! You are the Champion!")
elif player_score < computer_score:
    print("Computer wins this time!")
else:
    print("It's a tie overall!")