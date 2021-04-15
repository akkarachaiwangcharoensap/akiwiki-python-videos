print("Basic Boolean Algebra (De Morgan's theorem)")
print("What is the output of the followings?")

a = False;
b = True;

"""
if (a):
    print("a");
if (a and not a):
    print("a and not a");
if (a and not b):
    print("a and not b");
    
print("==================================");
"""

c = False;

if (a and not a and not(b and c) and (a and c)):
    print("Booya!");

else:
    print("Oh no!");
