# Write a program to read a file and count how many vowels are present in its content

# initial count 
count = 0
# open the file
with open("File.txt", "r") as file:
    content = file.read() # read files 
    print(content)

    for ch in content.lower(): # convert uppercase to lower case
        if ch in "aeiou":  # check conditions 
            count += 1

print("Total vowels:", count)
