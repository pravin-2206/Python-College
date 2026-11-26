import random as rd

guess=rd.randint(1,5)

userguess=int(input("Guess the number in between 1 to 5:"))

while userguess!=guess:
    print("Guess Number Wrong Try Again")
    userguess=int(input("Guess the number in between 1 to 5:"))
print("Right Guess ")