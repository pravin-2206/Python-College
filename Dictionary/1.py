student={
        101:{"Name":"Aditi","Scores":[93,80,79]},
        102:{"Name":"Rahul","Scores":[89,80,79]},
        103:{"Name":"Pravin","Scores":[80,75,89]},
        104:{"Name":"Om","Scores":[90,98,85]},
        105:{"Name":"Ram","Scores":[50,40,30]}
}

for sid, details in student.items():
        avg=sum(details["Scores"])/len(details["Scores"])
        details['Average']=avg
        details["Passed"]=avg>=50
        
print("Student how passed:")

for sid,details in student.items():
        if details["Passed"]:
                print(details["Name"])
        else:
                print(f'Fail Student',details["Name"])