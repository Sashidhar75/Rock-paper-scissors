import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Function to display the result and track scores
def play_game():
    # Initialize scores
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # Prompt user for input
        print("\nChoose rock, paper, or scissors:")
        user_choice = input("Enter your choice: ").lower()
        
        # Validate user input
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        # Computer makes a random choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chooses: {computer_choice}")
        
        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores based on the result
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        # Display scores
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Final Scores:")
            print(f"You: {user_score}, Computer: {computer_score}")
            break

# Run the game
if __name__ == "__main__":
    play_game()
