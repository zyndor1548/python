import random

print('This is a rock paper scissors game')
user = input('choose \nr for rock\np for paper\ns for scissors\n = ')
if user not in ['r', 'p', 's']:
  print('Invalid input. Please choose either r, p, or s.')
else:
  rint = random.randint(0, 3)
  if rint == 1:
    rps = 'r'
  elif rint == 2:
    rps = 'p'
  else:
    rps = 's'
  if rps == 'r':
    rpso = 'rock'
  elif rps == 's':
    rpso = 'scissors'
  else:
    rpso = 'paper'
  if user == 'r':
    usero = 'rock'
  elif user == 's':
    usero = 'scissors'
  else:
    usero = 'paper'
  print('system = ' + rpso)
  print('user = ' + usero)
  
  if user == rps:
    print('Draw!')
  elif (user == 'r' and rps == 's') or (user == 'p'and rps == 'r') or (user == 's'and rps == 'p'):
    print('User wins!')
  else:
    print('System wins!')