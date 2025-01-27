

# class Person:
#     # creat method(constructor )
#     def __init__(self, name, age=10):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute

#     def greet(self):

#         return f"Hello, my name is {self.name} and I am {self.age} years old."


# # creating instance of person class using constructor

# person1 = Person()
# print(person1.name)
# print(person1.age)

# print(person1.greet())

# using 'self' to call anyhor function

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

#     def details(self):
#         area = self.area()
#         perimeter = self.perimeter()

#         return f"Rectangle: width={self.width} height = {self.height} Area= {area} perimeter= {perimeter}"


# rectangle1 = Rectangle(5, 20)

# print(rectangle1.details())

# rectangle1.width = 10
# print(rectangle1.details())

#######################################################

# using @property

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invaliad house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
