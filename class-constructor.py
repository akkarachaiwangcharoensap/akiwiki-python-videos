class Student ():
    def __init__(this, name, age):
        this.name = name;
        this.age = age;

    def myName (this):
        return this.name;

    def myAge (this):
        return this.age;
        
studentA = Student("Aki", 21);
studentB = Student("Bob", 39);

print(studentA.myName());
print(studentA.myAge());

print(studentB.myName());
print(studentB.myAge());
