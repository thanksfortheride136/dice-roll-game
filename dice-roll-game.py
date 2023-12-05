#Library Imports
import random
import time

#opening info
def greeting():
  name = input("What is your name: " + "\n")
  print("Welcome to the dice roll game, " + name + "\n")
  user_dice_roll = input("Press x to roll the dice ")
  return user_dice_roll

user_dice_roll_input = greeting()

#Dice roll function
def dice_roll(user_input, user):
  while (user_dice_roll_input == 'x'):
    print(user + " rolls the dice.. ")
    roll = random.randint(1, 10)
    print(user + " rolls a " + str(roll))
    return roll

user_roll = dice_roll(user_dice_roll_input, "Louis")
computer_roll = dice_roll(user_dice_roll_input, "Computer")

#conditional function to choose winner
def choose_winner():
  if(user_roll < computer_roll):
    print("Computer Wins")
  elif (user_roll > computer_roll):
    print("User Wins")
  else:
    print("Its a tie")
    
#print statement
overall_result = choose_winner()
