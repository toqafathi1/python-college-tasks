
# def hello(to="world"):
#     print("Hello,", to)


# hello()
# name = input("What's your name?")
# hello(name)
################################

# def main():
#     name = input("What's your name?")
#     hello(name)
#     hello()


# def hello(to="world"):
#     print("Hello,", to)


# main()
################################################################

# def main():
#     x = int(input("enter the numeber"))
#     print("x squered", square(x))


# def square(n):
#     return n * n


# main()
#################################################

# def main():
#     x = int(input("Waht's x? "))
#     if is_even(x):
#         print("even")
#     else:
#         print("Odd")


# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# main()
################################################

#  using arguments

# def hello(*people):
#     for n in people:
#         print(f"Hello {n} ")


# hello("toqi", "yassin", "ahmed")

################################################

# using kwargs it's type dictionary

# def show_skills(**skills):

#     for skill, values in skills.items():
#         print(f"{skill} => {values}")


# show_skills(Html="60%", css="70%", python="30%")
################################################

# function recursion

def cleanWorld(world):

    if len(world) == 1:

        return world

    if world[0] == world[1]:

        return cleanWorld(world[1:])

    return world[0] + cleanWorld(world[1:])


print(cleanWorld("wwwwoooorrlddd"))
################################################

# import os
# # print abslout path
# print(os.path.abspath(__file__))
# print(os.getcwd)

################################

# map

# def formatText(text):

#     return f"- {text} -"


# myText = ["toqi", "mike", "john"]

# myFormatedText = map(formatText, myText)

# for text in myFormatedText:
#     print(text)

################################################

# filter return True values

# def checkName(name):
#     return name.startswith("O")


# mytext = ["Omer", "Ossy", "toqi"]

# myReturn = filter(checkName, mytext)

# for text in myReturn:
#     print(text)

################################################

# import sys
# print(sys.path)

################################


# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")


# def get_name():
#     return input("Name: ")


# def get_house():
#     return input("House: ")


# if __name__ == "__main__":
#     main()

################################################

# def main():
#     name, house = get_students()
#     print(f"{name} from {house}")


# def get_students():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house


# if __name__ == "__main__":
#     main()

################################################
# using tuples

# def main():
#     student = get_students()
#     print(f"{student[0]} form {student[1]}")


# def get_students():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house)


# if __name__ == "__main__":
#     main()

# using lists

# def main():
#     student = get_students()
#     print(f"{student[0]} form {student[1]}")


# def get_students():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]


# if __name__ == "__main__":
#     main()

# using dic

# def main():
#     student = get_students()
#     print(f"{student['name']} form {student['house']}")


# def get_students():
#     student = {}
#     student['name'] = input("Name: ")
#     student['house'] = input("House: ")
#     return student


# if __name__ == "__main__":
#     main()
