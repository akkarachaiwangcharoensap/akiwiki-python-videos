# Looping through each element
items = ["itemA", 123, False];
for item in items:
    print(item);

print("=============================");

# Looping through each element via index
for index in range(len(items)):
    print(items[index]);

print("=============================");

# Breaking a loop
for item in items:
    if (item == 123):
        break;

    print(item);

print("=============================");

# Ignoring or skipping a loop
for item in items:
    if (item == "itemA"):
        continue;

    print(item);

print("=============================");

# Loop 4 times
for index in range(0, 4):
    print(index);

print("=============================");

# Loop at a specific point
for index in range(24, 68, 1):
    print(index);

print("=============================");
print("|       Application!        |");
print("=============================");

print("=== ELEMENT FINDER ====");
inventory = ["itemA", "sword", "bow", "arrows"]
for item in inventory:
    if (item == "sword"):
        print("Sword is found!");
        break;

print("=== MIN or MAX ELEMENT FINDER ====");

listOfIntegers = [0,2,631,1231,52,123,-5215,25,-12312,81231,9999,-123123];

print("=== MIN ===");

smallest = listOfIntegers[0];

for item in listOfIntegers:
    if (smallest > item):
        smallest = item;

print("The smallest integer is " + str(smallest));

print("=== MAX ===");
largest = listOfIntegers[0];

for item in listOfIntegers:
    if (largest < item):
        largest = item;

print("The largest integer is " + str(largest));















