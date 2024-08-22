#Odd Even
num=int(input("enter num:"))
if num % 2 == 0:
    print("even")
else:
    print("odd")



#Printing given string under conditions
num=int(input("Enter a number: "))
if num %3==0 and num %5 ==0:
    print("fizzbuzz")
elif num  %3==0:
    print("fizz")
elif num %5==0:
    print("buzz")
else:
     print(num)