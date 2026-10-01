
# remove the duplicate element in list
l = [10, 20, 30, 20, 31]

new = []

for i in l:
    if i not in new:
        new.append(i)

print(new)