#mutable datatypes
#closed with []
#built in function list()
#unlike array it can have different datatypes

c=[1,2,3.4,"a","b",{1,2},[3,4]]


#Accessing lists elements
vowels=["a","e","i","o","u"]
print(vowels[0])#a
print(vowels[4])#u
print(vowels[10])#nthg(index error)
print(vowels[-2])#o
print(vowels[-1])#u
print(vowels[-10])#nthg

#slicing
vowels=["a","b","c","d","e","f","g","h","i","j"]
print(vowels[0:8])
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(vowels[2:7])
['c', 'd', 'e', 'f', 'g']
print(vowels[7:3])
[]
print(vowels[4:9])
['e', 'f', 'g', 'h', 'i']
print(vowels[5:])
['f', 'g', 'h', 'i', 'j']
print(vowels[-9:-2])
['b', 'c', 'd', 'e', 'f', 'g', 'h']
print(vowels[-2:-8])
[]
print(vowels[-3:])
['h', 'i', 'j']
print(vowels[:-2])
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

