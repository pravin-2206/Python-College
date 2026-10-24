dic={
        'name':'pravin',
        'age':21
}
dic['last']='nangare'
print(dic)
print(dic.values())
print(dic.keys)
#print(dic[0])
print(dic['last'])
print(dic['age'])


# list comprehension 

# find the cube of numbers up to 10

cube=[i**3 for i in range (11) if i%2==0]
print("cube of even number:",cube)

# read a file containing student names (one per line) and store them in a list.
 
 
with open('file.txt','r') as f:
        #read=f.readlines()
        read=[line.strip() for line in f]
print(read)
         
# Print names longer than 5 characters. 


with open('file.txt','r') as f:
        name=f.readlines()
        #print("s")
        if len(name)>5:                
                print(name)
                

# Count how many names start with a vowel 

# with open('file.txt','r') as f:
#         read=f.readlines()
#         count=0
#         if read in 'aeiou':
#                 count+=1
# print(count)

with open('file.txt', 'r') as f:
    read = f.readlines()
    count = 0

    for name in read:
        name = name.strip()
        if name and name[0].lower() in 'aeiou':
            count += 1

print(count)

# decorators is a function it takes another function as arguments and return function

def myfunction(func):
        def wrapper():
                print('initial transaction')
                func()
                print('transaction complated') 
        return wrapper
@myfunction
def hello():
        print('execute all step of transactions')
hello()
           
# anothe example
print("new example \n")

def secondfunction(fuc):
        def mxf(*args,**kwargs):
                print("Good morning")
                fuc(*args,**kwargs)
                print("Thank u for using this function")
        return mxf
@secondfunction
def add(a,b):
         print(a+b)
add(10,30)
# @secondfunction
# def hello():
#         print("hello guys!")
# hello()
# secondfunction(hello)()

# simple example 
def create():
        l=[]
        count=1
        while count<=100:
                l.append(count)
                count+=1
        return l
print(create())

print("generators example")

def creater():
        i=1
        while i<100:
                yield i # yield keyword is used to generate one value 
                i+=1
print(creater())
x=creater()
print(x) # its create object 
print(next(x)) # if u wont the value then next is used
print(next(x))

# if u wont all numbers then use list 
print(list(x)) # but it start with 3 number 




                
        

 
