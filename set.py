# Readable: can read during runtime/compile time
# Writeable: can write during  runtime and compile time

"""
 ============
|     Set    |
 ============

Readable

Not Ordered
No index
No duplicated values
Cannot modify the value during the runtime
but can add a new element

"""

fooSet = {"fooSetItem", False, 123};
anotherSet = set(("anotherSetItem", True, 456));
duplicatedSet = {123,456,123};

print(fooSet);
print(anotherSet);
print(duplicatedSet);

print ("===================================");

# Accessing an element can only be done via iteration
for item in fooSet:
    if (item == "fooSetItem"):
        print ("'fooSetItem' exists");

# Adding a new element to the set
fooSet.add("new set item");

# Removing an element at a value from the set
fooSet.remove("fooSetItem");

print ("===================================");

print("New modified set: ");
print(fooSet);
