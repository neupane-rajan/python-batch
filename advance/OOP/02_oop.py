"""
# instance variable vs class variables


class Student:
    school = "Niijo academy"  #class variable(shared)

    def __init__(self, name):
        self.name = name  # instance variable(unique)


s1 = Student("dhirendra")
s2 = Student("Shirish")
s3 = Student("Bharat")

print(s1.name)
print(s2.name)
print(s3.name)



# defining class  variable


class Employee:
    # class variable
    company = "Niijo Tech Pvt. Ltd."
    total_employees = 0

    def __init__(self, name, salary):
        # instance variable unique - to each employee
        self.name = name
        self.salary = salary
        Employee.total_employees += 1


e1 = Employee("Dhirendra", 50)
e2 = Employee("Bharat", 51)
e3 = Employee("sirish", 55)
# Employee.company = "Niijo"
e1.company = "niijo"

print(e1.company)
print(Employee.company)
# we can eccess calss variable using two ways:
# 1. via the class name
# 2. via an instance


"""

# modifying class variable

class Team: 
    # members = []  #mutable list
    
    def __init__(self,name):
        self.name = name
        self.members=[]

    def add_member(self,person): # instance method
        self.members.append(person)

t1 = Team("Team A")
t2 = Team("Team B")

t1.add_member("bharat")
t2.add_member("hello")
print(Team.add_member(t1))
