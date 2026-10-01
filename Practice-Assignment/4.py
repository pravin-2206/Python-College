# sen = input("Enter the sentence: ")

# count = 0
# l = len(sen)

# for i in range(l):
#     if sen[i] in "aeiouAEIOU":
#         count = count + 1

# print("Vowels:", count)


sen = input("Enter the sentence: ")

count1 = 0
count2= 0
count3=0
count4=0
count5=0
l = len(sen)

for i in range(l):
    if sen[i] in "aA":
        count1 = count1 + 1
    if sen[i] in "eE":
            count2=count2+1
    if sen[i] in "iI":
                count3=count3+1
    if sen[i] in "oO":
                count4=count4+1 
    if sen[i] in "uU":
                count5=count5+1

print(f'Count of A {count1}') 
print(f'Count of E {count2}')
print(f'Count of I {count3}')
print(f'Count of O {count4}')
print(f'Count of U {count5}')