# Your task is to create a program which will play Rock Paper Scissors with the user. Take input from the user for his/her selection like scissors/rock/paper. Program should select randomly rock/paper/scissors. Output should be indicating who won the user or computer. 


# Input from user: scissors
# Random selection from computer: paper
# Output: User won

# Input from user: rock
# Random selection from computer: paper
# Output: Computer won
import random

def play_game () : 
    userChoice = input(f'Enter Your Choice "rock/paper/scissors" : ').lower()
    choices = ['rock' , 'paper' , 'scissors']
    computerChoice = random.choice(choices)
    print('Computer Choice is :' , computerChoice)
    print('User Choice is :', userChoice)
    if computerChoice == userChoice : 
        print('Match Tie.')
    elif (
        (userChoice == 'rock' and computerChoice == 'scissors') or 
        (userChoice == 'paper' and computerChoice == 'rock') or 
        (userChoice == 'scissors' and computerChoice == 'paper')
    ) : 
        print('User Won')
    else : 
        print('Computer Won')


play_game()