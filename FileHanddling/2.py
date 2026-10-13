# Read all lines from a file into a list print the total number of lines and display the 2nd and 4th line


with open("file2.txt", "r") as file:  # open file 
    lines = file.readlines()   # read the file

print("Total number of lines:", len(lines)) # print total count of file

print("2nd line:", lines[1])  # print second line
print("4th line:", lines[3]) # print fourth line
