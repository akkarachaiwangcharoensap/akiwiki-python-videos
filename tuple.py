# Readable: can read during runtime/compile time
# Writeable: can write during  runtime and compile time

"""
 ============
|    Tuple   |
 ============

Readable

Not writeable:
    - cannot modify value, add or remove an element during the runtime.

"""

fooTuple = ("fooTupleItem", True, 123);
anotherTuple = tuple(("anotherTupleItem", False, 456));

print(fooTuple)
print(anotherTuple)

print ("===================================");

# Accessing an element based on given index
# List index starts at 0.
print(fooTuple[1]); # print the second element
print(anotherTuple[0]); # print the first element

print ("===================================");

print("New modified tuple: ");
print(fooTuple);
