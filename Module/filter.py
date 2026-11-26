# filter 

marks = [75, 80, 95, 45, 35, 89, 60]

def failing(marks):
    return marks<60

result=filter(failing,marks)
print("failing :",list(result))