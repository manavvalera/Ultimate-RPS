import random
import os
import time

# Define the choices and winning combinations
CHOICES = ["rock", "paper", "scissors"]
WINNING_COMBOS = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(CHOICES)

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif WINNING_COMBOS[player] == computer:
        return "win"
    else:
        return "lose"

# Function to play a single round
def play_round():
    while True:
        player_choice = input("\nEnter your choice (rock, paper, scissors): ").strip().lower()
        if player_choice in CHOICES:
            break
        print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
    
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {player_choice}")
    time.sleep(0.5)
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(player_choice, computer_choice)
    if result == "tie":
        print("\nIt's a tie! 🤝")
    elif result == "win":
        print("\nYou win! 🎉")
    else:
        print("\nYou lose! 😢")
    
    return result

# Function to play a best-of series
def play_best_of_series():
    wins = 0
    losses = 0
    ties = 0
    
    print("\n🏆 Best of 3 or 5 Mode!")
    while True:
        best_of = input("\nDo you want to play best of 3 or 5? (3/5): ").strip()
        if best_of in ['3', '5']:
            best_of = int(best_of)
            break
        print("Invalid input! Please enter '3' or '5'.")
    
    rounds_to_win = (best_of // 2) + 1
    
    while wins < rounds_to_win and losses < rounds_to_win:
        result = play_round()
        if result == "win":
            wins += 1
        elif result == "lose":
            losses += 1
        else:
            ties += 1
        
        print(f"\nScore: You {wins} - {losses} Computer (Ties: {ties})")
    
    if wins > losses:
        print("\n🏆 You won the series! Congratulations! 🎯")
    else:
        print("\n😔 You lost the series! Better luck next time!")

# Main function to run the game
def main():
    print("\n🎮 Welcome to Ultimate RPS!")
    time.sleep(0.5)
    
    while True:
        print("\nGame Modes:")
        print("1. Single Round")
        print("2. Best of 3 or 5")
        print("3. Quit")

        choice = input("\nSelect a mode (1/2/3): ").strip()
        
        if choice == '1':
            play_round()
        elif choice == '2':
            play_best_of_series()
        elif choice == '3':
            print("\nThanks for playing Ultimate RPS! 👋")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
        
        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if play_again in ['yes', 'no']:
                break
            print("Invalid input! Please enter 'yes' or 'no'.")

        if play_again == 'no':
            print("\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
