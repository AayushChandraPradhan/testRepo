#methods are smthg that are called by objects
#print()is function whereas
#a="blah" and a.capitalize is a method
a="Hello World I am learning Python"
result=a.split("e")
print(result)

data=["Hello","World","I","am","learning","Python"]
result=" ".join(data)
print(result)
result="+".join(data)
print(result)

#String Operations
#1.concatenation
#you can use membership operators in sequential data types like string, list, dictionary ,sets
#2.Repeatation
#"python"*3 ko ans is pythonpythonpython
#3.Membership
print("h".upper() in "Hello")
