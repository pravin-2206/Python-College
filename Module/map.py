# map() is a built-in function that applies a given function to every element of an iterable (like a list or tuple).


marks = [75, 80, 95, 45, 35, 89, 60]

def grade(marks):
    if marks >= 90:
        return "A"
    elif 80 <= marks < 90:
        return "B"
    elif 70 <= marks < 80:
        return "C"
    elif 36 <= marks < 70:
        return "D"
    else:
        return "Fail"

result = map(grade, marks)

print("Marks",marks)
print(list(result))