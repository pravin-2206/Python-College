import datetime

current=datetime.datetime.now()  # datetime.now() function return current date and time 
print(current)

print(current.strftime('%Y')) # only display year of date

print(current.strftime('%b')) # display month in short word dec

print(current.strftime('%B')) # display month full name december

print(current.strftime('%m')) # display month as number 

print(current.strftime('%y')) # display year in short like 26

print(current.strftime('%Y')) # display year full like 2026

print(current.strftime('%H')) # display only hour 

print(current.strftime('%M')) # display minutes

print(current.strftime('%S')) # display seconds 

print(current.strftime('%p')) # display PM

print(current.strftime('%a')) # week of day
