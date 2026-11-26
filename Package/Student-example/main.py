from Student.details import student_info
from Student.marks import calculate_percentage 
from Student.marks import calculate_total

print(f"Student Information:",student_info('Pravin'))
print(f'Student Marks total',calculate_total(100,98,69))
print(f'Student Marks total',calculate_total(50,45,90))

print(f'Student Percentage',calculate_percentage(58,68,99))
