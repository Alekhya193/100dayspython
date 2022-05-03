# rock paper scissor
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
player=int(input())
if(player==0):
    print(rock)
elif (player==1):
    print(paper)
else:
    print(scissors)

print("computer choose:")
computer=random.randint(0,2)
if(computer==0):
    print(rock)
elif (computer==1):
    print(paper)
else:
    print(scissors)
if((player>=3 or player<0) or (computer>=3 or player<0) ):
    print("enter valid number")
else:

 if(player==0 and computer==2 ):
    print("you won!")
 elif(player==2 and computer==0 ):
    print("you lose!")
 elif(computer>player):
    print("you lose!")
 elif(computer<player):
    print("you win!")
 elif(computer==player):
    print("its tie")

