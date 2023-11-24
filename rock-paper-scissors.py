import random

def get_user_choice():
    print("Enter your choice: Rock, Paper, or Scissors")
    user_choice = input().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors game!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice.capitalize()}")
        print(f"Computer chose {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        print("Do you want to play again? (yes/no)")
        play_again = input().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    rock_paper_scissors()
