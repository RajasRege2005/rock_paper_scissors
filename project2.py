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

import random
choice=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
if choice=='0':
  print(rock+"\n")
  print("Computer chose:\n")
  random1=random.randint(0,2)
  if random1==0:
    print(rock+"\n")
    print("It's a draw")
  elif random1==1:
    print(paper+"\n")
    print("You lose")
  else:
    print(scissors+"\n")
    print("You win")
elif choice=='1':
  print(paper+"\n")
  print("Computer chose:")
  random1=random.randint(0,2)
  if random1==0:
    print(rock+"\n")
    print("You win")
  elif random1==1:
    print(paper+"\n")
    print("It's a draw")
  else:
    print(scissors+"\n")
    print("You lose")
else:
  print(scissors+"\n")
  print("Computer chose:")
  random1=random.randint(0,2)
  if random1==0:
    print(rock+"\n")
    print("You lose")
  elif random1==1:
    print(paper+"\n")
    print("You Win")
  else:
    print(scissors+"\n")
    print("It's a draw")