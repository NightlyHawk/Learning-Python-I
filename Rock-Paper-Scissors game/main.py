import random
import os
import sys

def game():

 moves = ["rock","paper","scissors"]
 Player = input ('your turn. \n')
# def random_word(words):
#     return random.choice(moves)

 Computer = print(random.choice(moves))
 while True:
  if Player == Computer:
    print('draw')    
  elif Player == "rock":
    if Computer == "paper":
     print('Computer wins \n')
    else:
     print('You win \n')
  elif Player == "paper":
    if Computer == "rock":
      print('You win \n')
    else:
      print('Computer wins \n')
  elif Player == "scissors":
    if Computer == "rock":
     print('Computer wins \n')
    else: 
      print('You win \n')
#  elif Player != "rock":
#    if Player != "paper":
#      print('unavailable move \n') 
 else:
      print('unavailable move \n') 
   
        
    # os.execl(sys.executable, sys.executable, *sys.argv)

game()
