# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from cgitb import text
from tkinter import N


def read_file_content(a):
    # [assignment] Add your code here 
    with open(a) as f:
     contents = f.read()
    
    print(contents)

def count_words():
    text = read_file_content('story.txt')
    # [assignment] Add your code here
    print(text.count("as", "would"))

count_words()

