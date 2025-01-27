

# class Member:
#     # methods function inside class
#     def __init__(self, first_name, last_name):

#         self.fname = first_name
#         self.lname = last_name
# # instance method

#     def full_name(self):

#         return f"{self.fname} {self.lname}"


# # studet1 =>  instance
# student1 = Member("toqi", "fathi")

# print(student1.full_name())


################################################################

# class Student:
#     # instance method
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ranvenclaw"]:
#             raise ValueError("Invalide house")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     # creat object from class
#     # student = Student()
#     # student.name = input("Name: ")
#     # student.house = input("House: ")
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)


# if __name__ == "__main__":
#     main()
#####################################################

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


class MinimumBalance(BankAccount):
    def __init__(self, minimum_balance):
        # BankAccount.__init__(self)
        super().__init__()
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be mintained')
        else:
            BankAccount.withdraw(self, amount)


account = MinimumBalance(100)

account.deposit(200)
account.withdraw(50)
print(account.balance)

# class Canvas:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.data = [[' '] * width for i in range(height)]

#     def setpixel(self, row, col):
#         self.data[row][col] = '*'

#     def getpixel(self, row, col):
#         return self.data[row][col]

#     def display(self):
#         print("\n".join(["".join(row) for row in self.data]))


# class Shape:
#     def paint(self, canvas): pass


# class Rectangle(Shape):
#     def __init__(self, x, y, w, h):
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h

#     def hline(self, x, y, w):
#         pass

#     def vline(self, x, y, h):
#         pass

#     def paint(self, canvas):
#         self.hline(self.x, self.y, self.w)
#         self.hline(self.x, self.y + self.h, self.w)
#         self.vline(self.x, self.y, self.h)
#         self.vline(self.x + self.w, self.y, self.h)


# class Square(Rectangle):
#     def __init__(self, x, y, size):
#         Rectangle.__init__(self, x, y, size, size)


# class CompoundShape(Shape):
#     def __init__(self, shapes):
#         self.shapes = shapes

#     def paint(self, canvas):
#         for s in self.shapes:
#             s.paint(canvas)
