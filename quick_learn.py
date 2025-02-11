

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


# using modules
