# read a file, split its content into words and store them in a list 

# 1 print the total number of words
# 2 print all unique words



# Read a file and split its content into words
with open("File.txt", "r") as file:
    content = file.read()  # Read all content from the file

words = content.split()  # Split content into words and store in a list

# 1. Print the total number of words
print("Total number of words:", len(words))

# 2. Print all unique words 
unique_words = set(words)

print("Unique words:", unique_words)
