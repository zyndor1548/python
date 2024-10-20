import random
print ("This is a password generator")
sample = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQESTUVWXYZ1234567890!@#$%^&*_-"
password = ''
for i in range(int(input('pasword length: '))):
  password += sample[random.randint(0, 71)]
print('password = ' + password)