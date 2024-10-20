import random
print('by aromal')
sample = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQESTUVWXYZ1234567890!@#$%^&*_-"
password =''
for i in range(int(input('pasword length: '))):
    password += sample[random.randint(0,71)]
print('password = '+ password)
