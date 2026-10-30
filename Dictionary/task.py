# # write a program to guees number 
# import random
# num=int(input("Enter the number"))
 
# guess=random.random()


import random
# range between 1 to 10 
number = random.randint(1, 10)

guess = int(input("Guess the number (1-10): "))

if guess == number:
    print("Correct ")
else:
    print("Wrong The number ", number)