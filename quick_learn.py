import math
import random

# LISTS ======== Ordered, mutable (changeable) sequences
my_list = [1, 2, "hello", 3.14]
my_list.append(5)
print(my_list[0])

# TUPLES ======== Ordered, immutable (unchangeable) sequences
my_tuple = (1, 2, "hello", 3.14)
print(my_tuple)

# DICIONARIES ======== Unordered, mutable (changeable) collection of key-value pairs
my_dict = {"name": "John", "age": 25}
print(my_dict["name"])

# FOR loops
for i in range(1, 5):
    print(i);

for item in my_list:
    print(item);

# while loops
i = 0
while i < 5:
    print(i);
    i += 1

# FUNCTIONS
def greet(name):
    print(f"Hello, {name}"); # you can also concatenate using the + operator

greet("John")


# ===== using modules
result = math.sqrt(16)
print(int(result)); # coverted to  integer


random_number = random.randint(1, 10);
print(random_number); 


# OOP
class Dog: 
    def __init__(self, name, breed): #constructor
        self.name = name;
        self.breed = breed;

    def bark(self):
        print(f"{self.name} Woof!");

dog_1 = Dog("Rex", "German Shepherd");
dog_1.bark(); # Rex Woof!
print(dog_1.breed)

