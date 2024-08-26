#develop a simple game of stone paper scissor with one player as computer and another as a user

#matrix to define results               0     1      2
# stone_paper_scissor =               Stone Paper Scissor
#                       0     Stone     D     L      W
#                       1     Paper     W     D      L
#                       2     Scissor   L     W      D

#Column is represnting inputs of computer and row is representing user input
#the matrix values are represented for user,if he/she wins(W),Lose(L) or Draw(D)

import random
import keyboard
import sys
stone_paper_scissor = [['D','L','W'],
                       ['W','D','L'],
                       ['L','W','D']]

print('Press q s(Quit) to exit...!')

inputs = {0:'Stone',1:'Paper',2:'Scissor'}
while True:
    computer_input = random.randint(0,2)
    print('\n0. Stone, 1. Paper, 2. Scissor, 3. Exit')
    user_input = int(input('Enter your choice: '))
    if user_input == 3:
        print('\nThank you for playing')
        sys.exit()
    print('Computer input: ',inputs[computer_input])
    print('Your input: ',inputs[user_input])

    result = stone_paper_scissor[user_input][computer_input]
    if result == 'D':
        print('\ngame has been drawn')
    elif result == 'W':
        print('\nYou won the game')
    else:
        print('\nOops... You lose the game')

    

