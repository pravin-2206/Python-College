#LC1089:
def duplicateZeros(arr):
    n = len(arr)
    temp = []
    for i in range(n):
        temp.append(arr[i])
        if arr[i] == 0:
            temp.append(0)
    for i in range(n):
        arr[i] = temp[i]
    return  arr

arr = [1, 0, 2, 3, 0, 4, 5, 0]
print("Array now is: ", arr)
duplicateZeros(arr)
print("Array after duplicating is: ", arr)