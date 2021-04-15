def recursiveFunction (i):
    if (i == 0):
        return;

    print(i);
    recursiveFunction(i - 1);
    print(i);

recursiveFunction (10);

print("==========================");

def factorialFunction (i):
    if (i == 1):
        return 1;

    return i * factorialFunction(i - 1);

print(factorialFunction(5));
