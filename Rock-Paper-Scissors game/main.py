import random



moves = ["rock","paper","scissors"]
Player = input ('your turn. \n')


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

   else:
       print('unavailable move \n') 
   
        
  
   play_again = input("Play again? (y/n): ")
   if play_again.lower() != "y":
        break
