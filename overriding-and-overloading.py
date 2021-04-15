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

class GradeAStudent (Student):
    def __init__(this, name, age, gpa, wealth):
        super().__init__(name, age, gpa);

        this.gpa = 4.0;
        this.wealth = "Outstanding"

    def myName (this, title):
        return title + this.name;
    
    def myGPA (this):
        return this.gpa;

    def myWealth (this):
        return this.wealth;

class Teacher(Person):
    def __init__(this, name, age, reviews):
        # calling parent's constructor function
        super().__init__(name, age);

        this.reviews = reviews;

    def myReviewScore (this):
        return this.reviews;

aki = Student("Aki", 21, 2);
bob = Teacher("Bob", 39, 4.5);

smartass = GradeAStudent("Foo", 15, 4123123, "poor");

print(aki.myName());
print(aki.myAge());
print(aki.myGPA());

print("============================")

print(bob.myName());
print(bob.myAge());
print(bob.myReviewScore());

print("============================")

print(smartass.myName("Ms."));
print(smartass.myAge());
print(smartass.myGPA());
print(smartass.myWealth());

