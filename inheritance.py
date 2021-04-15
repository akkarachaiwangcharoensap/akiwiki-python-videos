class Person:
    def __init__(this, name, age):
        this.name = name;
        this.age = age;

    def myName (this):
        return this.name;

    def myAge (this):
        return this.age;

class Student(Person):
    def __init__(this, name, age, gpa):
        # calling parent's constructor function
        super().__init__(name, age);

        this.gpa = gpa;

    def myGPA (this):
        return this.gpa;

class Teacher(Person):
    def __init__(this, name, age, reviews):
        # calling parent's constructor function
        super().__init__(name, age);

        this.reviews = reviews;

    def myReviewScore (this):
        return this.reviews;

aki = Student("Aki", 21, 2);
bob = Teacher("Bob", 39, 4.5);

print(aki.myName());
print(aki.myAge());
print(aki.myGPA());

print(bob.myName());
print(bob.myAge());
print(bob.myReviewScore());

