# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True
# word = ['stop', 'pots']
from re import X
from tkinter import Y

x = input ('type word \n')
y = input ('type second word \n')
# def find_anagrams(x,y):
#     # [assignment] Add your code here
if (sorted(x) == sorted(y)):
 print(True)

else: 
 print(False) 
    # find_anagrams('stop','pots')