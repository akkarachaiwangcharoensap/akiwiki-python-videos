# Readable: can read during runtime/compile time
# Writeable: can write during  runtime and compile time

"""
 ============
| Dictionary |
 ============
 
No index
No duplicates are allowed
Readable
Writeable

"""

fooDictionary = {
    "keyA" : "valueA",
    "keyB" : "valueB",
    "keyC" : 123,
    "keyD" : False,
    "keyF" : ["a", "b", "c"]
};

duplicatedDictionary = {
    "keyA" : "valueA",
    "keyB" : "valueB",
    "keyC" : 123,
    "keyD" : False,
    "keyA" : "THIS IS NOT ALLOWED"
};

print(fooDictionary);
print(duplicatedDictionary);

print ("===================================");

# Accessing an element based on given value
print(fooDictionary["keyA"]);
print(fooDictionary["keyF"]);

# Creating a new key to the dictionary
fooDictionary["newKey"] = "some new value";

# Removing an element at a specific key
del fooDictionary["keyB"];

print ("===================================");

print("New modified dictionary: ");
print(fooDictionary);


