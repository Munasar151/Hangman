#imports
import os
import time


#variable values
from operator import truediv
from re import A

n = "Munasar"
lives = 3
guessed = []
correct = []
deny = False
x = 0
missing = "-"*len(n)
change = ""

#check if lives is more than 0
while lives>0:
  x = 0
  y = 0
  count = 0
  deny = False
  #replace the hyphens with the correctly guessed letters counterpart
  while y < len(n):
    z=0
    accept = True
    while z < len(correct):
      if n[y].lower() == correct[z].lower():
        
      
        print(correct[z], end="")
        accept = False
        count+=1

    
      z+=1
      if z == len(correct) and accept == True:
        print("-", end="")
    y+=1

#check if the answer is found 
  if count == len(n):
    
    print("\n********Congratulations, you have guessed the word correctl*****")
    print("You still had " + str(lives) + " left.")
    break

  #get the user's guess
  print("\nPlease enter a letter: ")
  letter = str(input())
  
  #only accept one letter
  if len(letter) == 1 and letter.isalpha() == True:

    #check if the guess is correct and do not allow the user to guess the same letter again
    if letter.lower() in n.lower():
      while x < len(correct):
        if correct[x] == letter:
          deny = True
          print("The letter has already been guessed correctly")
          time.sleep(1)
          break
        x+= 1

      #add a letter if the user has guessed another letter correctly
      if deny == False:
        correct.append(letter)
        print("\nYou have the following letters correct: ")
        time.sleep(1)

    #check if the guess is not correct and user does not lose a life if they guessed the letter incorrectly again
    if letter.lower() not in n.lower():
      while x < len(guessed):
        if guessed[x] == letter:
          deny = True
          print("The letter has already been used")
          time.sleep(1)
          break
        x+= 1
      
      #lose a life if the letter was guessed incorrectly and append the letter guessed incorrectly
      if deny == False:
        lives-=1
        print("\nCurrent lives: " + str(lives))
        time.sleep(1)
        guessed.append(letter)

    

  #deny the input if it is more than one letter and other values that are not in the alphabet
  else:
    print("Please only enter 1 letter")
    time.sleep(1)
  os.system("cls")

  #end the game if the user has lost all 3 lives
  if lives == 0:
      print("Game over.")