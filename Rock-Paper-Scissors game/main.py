import random
import os
import sys

def game():

 moves = ['R','P','S']
 Player = input ('your turn. \n')
# def random_word(words):
#     return random.choice(moves)

 Computer = input(random.choice(moves))

 if (Player == Computer):
    print('draw')    
 if (Player == moves[0].lower() and Computer.lower() == moves[1].lower() ):
    print('Computer wins \n')
 if (Player == moves[0].lower() and Computer.lower() == moves[2].lower() ):
    print('You win \n')
 if (Player == moves[1].lower() and Computer.lower() == moves[0].lower() ):
    print('You win \n')
 if (Player == moves[1].lower() and Computer.lower() == moves[2].lower() ):
    print('Computer wins \n')
 if (Player == moves[2].lower() and Computer.lower() == moves[0].lower() ):
    print('Computer wins \n')
 if (Player == moves[2].lower() and Computer.lower() == moves[1].lower() ):
    print('You win \n')
 if (Player != moves[0] or Player != moves[1] or Player != moves[2]):
    print('unavailable move \n') 
    while True: 
        game()
    # os.execl(sys.executable, sys.executable, *sys.argv)

game()
