# class method(@classmethod)
#  A class method receives the class itself as the  first parameter not an object or self


class Employee:
    total = 0

    def __init__(self, name):
        self.name = name
        Employee.total += 1

    @classmethod
    def get_total(cls):
        return f"total number of employees: {cls.total}"


# e1 = Employee("Dipak")
# e2 = Employee("Dhirendra")
# print(e1.get_total())


# static methods(@staticmethod)
# a static method doesn't receive self or cls.add(). it is just a regular function that lives inside a class.


class MathOperation:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def square(number):
        return number**2

print(MathOperation.is_even(1))


# things to remember
# it is decorated with @staticmethod
# there is not self or cls
# its atc like a regular function but grouped inside a class for context


# create a Validator class with static methods: is_email(s), is_phone(s), strong_password() each return true or false
