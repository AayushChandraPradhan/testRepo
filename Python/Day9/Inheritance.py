class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Ram", 19)
person1.get_details()


#QN no 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary, designation):
        super().__init__(name, age)
        self.salary = salary
        self.designation = designation

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Designation: {self.designation}")

e1 = Employee("Ram", 19, 150000, "Teacehr")
e1.get_details()  


class Circle:
    def __init__(self, radius):
        self.radius = radius

c1 = Circle(5)
c2 = Circle(7)

radius_sum = c1.radius + c2.radius

print(radius_sum)



# Inheritance is the way of accessing the attributes of parent class into
# the children classes

class Vehicle:
    engine_type = "Petrol"
    def __init__(self, color, company):
        self.color = color
        self.company = company

class Bike(Vehicle):  # Bike class is inheriting Vehicle Class
    no_of_wheels = 2


b = Bike()
print(b.engine_type)  # Petrol
print(b.doors)  # Attribute Error


# Types of Inheritance in Python
# 1. Single Inheritance
# 2. Multiple
# 3. MultiLevel
# 4. Hierarchical
# 5. Hybrid


# Single
class A:
    a = 1

class B(A):
    pass


# Multiple Inheritance
class A:
    a = 1

class B:
    b = 1


class C(A, B):
    pass

# Multilevel Inheritance
class A:
    x = 2  # 

    def __init__(self) -> None:
        pass


class C(A):
    c = 3  # class attribute

print(C.c)

class D(C):
    d = 4


# Hierarchical Inheritance
class A:
    a = 1

class B(A):
    b = 2


class C(A):
    c = 3

obj = C()


# Hybrid Inheritance
# It is the combination of hybrid and hierarchical inheritance

class A:
    a = 1

class B:
    a = 2

class C(A, B):  # Multiple inheritance
    pass

class D(C):
    a = 4

class E(C):
    pass

class F(E):
    pass


f_obj = F()
f_obj.a


# MRO (Method Resolution Order)
# It is the order in inheritance which defines the way to access the attributes
# Child first and left to right
