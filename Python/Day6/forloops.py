#loops
#for loop
#while loop

#1. For loop
#loops are used in sequential datatypes

a=[1,2,3,4,5]
for b in a:
    print(b)
    
#2. While loop
#They are used with truthy or falsy statement.It executes until statement is truthy.



# WAP to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number.


hour=int(input("Enter how much hours worked:"))
rate=float(input("Enter hourly rate:"))

if hour <= 40:
    pay=rate*hour
    print(pay)
    
elif hour >= 45:
    ot=hour - 40
    pay=40 * rate
    ot_pay=ot * rate *1.5
    gross_pay = pay  +ot_pay
    print(gross_pay)
    
    
    
student = {"name": "Jon", "age": 30, "address": "KTM"}s
for each in student:
    print(each)  # name   age   address

for key, value in student.items():
    print(key)  # name  age  address
    print(value) # Jon  30   KTM


for each in student.values():
    print(each)  # Jon  30  KTM