#append
a=[1,2,3]
a.append(4)
print(a)

a=[1,2,3]
result=a.append(4)
print(result) #it causes in error because result ma hunna since lists is mutable a mai change hunxa so print(a) works
#pop returns the value so same case gariyo bhane it works with pop

#extend
a=[1,2,3]
a.extend(4,5,6)
print(a)

#remove
a=["a","b","c"]
a.remove("b")
print(a)

#pop
a=["a","b","c"]
a.pop(1)
a.pop()
print(a)

#insert
a=["a","b","c"]
a.insert(1,"d")

#clear
a=["a","b","c"]
a.clear()
print(a)


#pass by reference mutable lists uses this
#pass by value immutable kura haru ma use hune
#a=1
# b=a
# print(a) garyo bhane 1 aauxa a and b both
# a=3
# and print a and b garyo bhane a and b both wont be same b ko value 1 nai hunxa a change bhayera 3

 
# copy()
a = [1, 2, 3]
b = a  # Pass by reference
a.append(4)
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]

b = a.copy()  # Pass by value
a.append(5)
print(a) # [1, 2, 3, 4, 5]
print(b)  # [1, 2, 3, 4]