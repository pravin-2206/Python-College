# take a sentence from the user split it into words and store them in list print the longest word


sentence = input("Enter a sentence: ") # input from user

words = sentence.split() # split the sentence 

longest = max(words, key=len)  

print("Words:", words) # print words
print("Longest word:", longest) # logest words
