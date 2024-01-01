# create a simple rock, paper, scissors game
# provide a welcome message
# get the user's choice
# get the computer's choice
# compare the choices and determine the winner
# display the results
# ask the user if they want to play again
# if not, exit the program
# if so, repeat the steps above

# Import the random module
import random

# Define a function to get the user's choice
def get_user_choice():
    # Initialize a variable to hold the user's choice
    choice = ''
    # Loop until the user enters a valid choice
    while choice.lower() not in ['rock', 'paper', 'scissors']:
        # Ask the user for their choice
        choice = input("Choose rock, paper, or scissors: ")
    # Return the user's choice
    return choice

# Define a function to get the computer's choice
def get_computer_choice():
    # Initialize a variable to hold the computer's choice
    choice = ''
    # Loop until the computer enters a valid choice
    while choice.lower() not in ['rock', 'paper', 'scissors']:
        # Generate a random number between 0 and 2
        choice_index = random.randint(0, 2)
        # Assign the choice based on the random number
        if choice_index == 0:
            choice = 'rock'
        elif choice_index == 1:
            choice = 'paper'
        else:
            choice = 'scissors'
    # Return the computer's choice
    return choice

# Define a function to compare the choices and determine the winner
def determine_winner(user_choice, computer_choice):
    # Initialize a variable to hold the winner
    winner = ''
    # Check if the user and computer made the same choice
    if user_choice == computer_choice:
        winner = 'tie'
    # Check if the user chose rock
    elif user_choice == 'rock':
        # Check if the computer chose paper
        if computer_choice == 'paper':
            winner = 'computer'
        # Otherwise, the computer chose scissors
        else:
            winner = 'user'
    # Check if the user chose paper
    elif user_choice == 'paper':
        # Check if the computer chose scissors
        if computer_choice == 'scissors':
            winner = 'computer'
        # Otherwise, the computer chose rock
        else:
            winner = 'user'
    # Otherwise, the user chose scissors
    else:
        # Check if the computer chose rock
        if computer_choice == 'rock':
            winner = 'computer'
        # Otherwise, the computer chose paper
        else:
            winner = 'user'
    # Return the winner
    return winner

# Define a function to display the results
def display_results(user_choice, computer_choice, winner):
    # Print the results
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    # Check if the game was a tie
    if winner == 'tie':
        print("The game was a tie.")
    # Otherwise, check if the user won
    elif winner == 'user':
        print("You won!")
    # Otherwise, the computer won
    else:
        print("The computer won!")

# Define a function to ask the user if they want to play again
def play_again():
    # Initialize a variable to hold the user's choice
    choice = ''
    # Loop until the user enters a valid choice
    while choice.lower() not in ['yes', 'no']:
        # Ask the user if they want to play again
        choice = input("Would you like to play again? Enter yes or no: ")
    # Return the user's choice
    return choice

# Define a function to play the game
def play_game():
    # Display a welcome message
    print("Welcome to Rock, Paper, Scissors!")
    # Initialize a variable to hold the user's choice
    user_choice = ''
    # Loop until the user enters a valid choice
    while user_choice.lower() not in ['rock', 'paper', 'scissors']:
        # Ask the user for their choice
        user_choice = input("Choose rock, paper, or scissors: ")
    # Get the computer's choice
    computer_choice = get_computer_choice()
    # Determine the winner
    winner = determine_winner(user_choice, computer_choice)
    # Display the results
    display_results(user_choice, computer_choice, winner)
    # Ask the user if they want to play again
    choice = play_again()
    # Check if the user wants to play again
    if choice.lower() == 'yes':
        # Play the game again
        play_game()

# Call the play_game function
play_game()

# Path: rockpaperscissors/game.py
# Compare this snippet from fibonacci/example.py:
# # This program generates a Fibonacci sequence up to n terms
#
# # Function to generate Fibonacci sequence
# def fibonacci(n):
#     # Initialize an empty list to hold the sequence
#     sequence = []
#     # The first two numbers in the Fibonacci sequence are 0 and 1
#     a, b = 0, 1
#     # Loop n times
#     for _ in range(n):
#         # Append the current number to the sequence
#         sequence.append(a)
#         # Update a and b to the next two numbers in the sequence
#         a, b = b, a + b
#     # Return the generated sequence
#     return sequence
#
# # Main program starts here
# while True:
#     # Ask the user for the number of terms in the sequence
#     n = input("Enter the number of terms in the Fibonacci sequence or 'exit', 'quit', 'q', 'e' to stop: ")
#     # Check if the user wants to exit the program
#     if n.lower() in ['exit', 'quit', 'q', 'e']:
#         break
#     # Generate the Fibonacci sequence up to n terms
#     fib_sequence = fibonacci(int(n))
#     # Print the generated sequence
#     print(fib_sequence)
# create a simple rock, paper, scissors game
# provide a welcome message
# get the user's choice
# get the computer's choice
# compare the choices and determine the winner
# display the results
# ask the user if they want to play again
# if not, exit the program
# if so, repeat the steps above

