def addFunction (a, b):
    return a + b;

myNumberA = 4;
myNumberB = 6;

print(addFunction(myNumberA, myNumberB));


# Pass by reference example!
def tryToModifyArgument (a, b):
    a = 25;
    b = 12;

tryToModifyArgument(myNumberA, myNumberB);

print(myNumberA);
print(myNumberB);


    
