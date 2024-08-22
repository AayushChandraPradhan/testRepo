#WAP to input a number and check whether a number is even or odd
num=int(input("Enter a number:"))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#WAP to input three numbers and find the greatest 
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))

if a>b:
    if a>c:
     print("a is greatest")

if b>a:
    if b>c:
        print("b is the greatest")  
        
if c>a:
    if c>b:
        print("c is the greatest")

# if num1 > num2 and num1 > num3:
#     print(f"{num1} is the greatest")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} is the greatest")
# else:
#     print(f"{num3} is the greatest")