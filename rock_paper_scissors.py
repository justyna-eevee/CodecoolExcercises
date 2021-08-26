import random


choices = ['rock', 'scissors', 'paper']

computer_points = 0
player_points = 0

while True:
    computer = random.choice(choices)
    player = input("""
    ENTER YOUR CHOICE
    rock
    paper
    scissors
    """)

    if player.lower() not in choices:
        print('Wrong choice!')
    elif computer == player.lower():
        print('Computer chose the same!')
    elif player.lower() == 'rock':
        if computer == 'paper':
            computer_points += 1
        else:
            player_points +=1
    elif player.lower() == 'scissors':
        if computer == 'rock':
            computer_points += 1
        else:
            player_points +=1
    elif player.lower() == 'paper':
        if computer == 'scissors':
            computer_points += 1
        else:
            player_points +=1


    print(f'Your score: {player_points}')
    print(f'Computer score: {computer_points}')

    next_game = input("""
    Do you want to play one more time?
    yes = Y
    no = N
    """).lower()
    
    if next_game == "n":
        if computer_points > player_points:
            print('Computer win!')
        elif player_points > computer_points:
            print('You win!')
        else:
            print('Draw!')
        break

