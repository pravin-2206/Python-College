# one block for multiple exceptions

try:
    num=int(input("Enter number"))
    re=100/num
    print(re)

except(ValueError,ZeroDivisionError):
    print("Invalind operation")