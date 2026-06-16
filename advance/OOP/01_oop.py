# a class is blueprint and an object is a thign that is created from that blueprint

# correct way of defining class
# Student
# StudentDetails
# OnlineCourse

# avoid
# student
# student_details
# Student_Details


class Student:

    # constructor
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"hello i am {self.name}. I am {self.age} years old")

    def average(self):
        self.average = sum(self.marks) / len(self.marks)
        print(f"average marks of {self.name} is {self.average}")


dip = Student("dipu", 21, [20, 21, 23, 40, 50])
dhirendra = Student("dhirendra", 21, [9, 9, 9, 9, 9])
# print(dip.marks)

# dip.average()


# create a class circle with attribute radius. Add methods area() and circumference() that calculate and return the values.


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.1415 * self.radius


calculate = Circle(23)

print(calculate.circumference())


# create a class rectange with width and height. add method area(),parameter(),and is_square()(return true if width == height else return false)


class Rectange:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def parameter(self):
        return 2 *(self.width + self.height)
    def is_square(self):
        if self.width == self.height:
            return True
        
        else:
          return False
        
calculate = Rectange()

calculate.area()

# create a class movie with attribute title, director , year rating.Add a method is_classic() that return true if the move is more than 25 years old.


# create a class Employee with name, salary and department.Add a method give_raise(amount) that increases salary. Create a 3 empoolyees and give of them raise.add()
# create a clas calculator with add(),subtract(), multiply(), divide(),
