# Readable: can read during runtime/compile time
# Writeable: can write during  runtime and compile time

"""
 ============
| List/Array |
 ============
 
Ordered
Readable
Writeable

"""

fooList = ["fooListItem", 123, True];
anotherList = list(("anotherListItem", 456, False));

print(fooList);
print(anotherList);

print ("===================================");

# Accessing an element based on given index
# List index starts at 0.
print(fooList[1]); # print the second element

# Adding a new element to the list
fooList.append("hello world");

# Removing an element at a specific index from the list
del fooList[0];

# Removing an element based on the value from the list
fooList.remove(123);

print ("===================================");

print("New modified list: ");
print(fooList);
