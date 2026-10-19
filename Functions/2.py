a=int(input("Enter first number:"))
b=int(input("Enter the Second Number:"))
def number(a,b):
        rem=a%b
        div=a//b
        return rem,div
result=number(a,b)
print(result)