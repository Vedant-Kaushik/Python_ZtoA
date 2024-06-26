import random

for i in range(0, 5):
  choices = {"snake": "1", "water": "2", "gun": "3"}


  my_choice = input('Enter snake, water, or gun : ')


  
  my_choice = choices[my_choice]  # Convert to numerical value using dictionary
#   print('You chose:', my_choice)

  options = ['1', '2', '3']
  random_choice = random.choice(options)
  print('Computer chose:', random_choice)

  if my_choice == random_choice:
    print('It\'s a draw!')
  elif (my_choice == '2' and random_choice == '1') or (my_choice == '3' and random_choice == '2') or (my_choice == '1' and random_choice == '3'):
    print('You win!')
  else:
    print('You lose!')
