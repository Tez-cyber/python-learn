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
    print(i)

for i in range(5, 10):
    print(i * 5)

for item in my_list:
    print(item)