
# basics of lists
# fruits = ["apple", "banana", "graps", "pinapple"]
# new_fruits = []
# for i in fruits:
#     print(i)
# fruits.reverse()
# print(fruits)

# fruits.append("orange")
# print(fruits)

# use extend to add all the items of an iterable
# numbers = [1, 3, 5]
# even_numbers = [2, 4, 6]

# numbers.extend(even_numbers)
# print(numbers)

# use insert to add an element at specified index
# numbers.insert(3, 7)
# print(numbers)

# change list item
# numbers[3] = 9
# print(numbers)

# remove item from list
# numbers.remove(9)
# print(numbers)

# fruits.sort()
# print(fruits)
# li = [-6, -5, -4, 1, 2, 3]
# s_li = sorted(li, key=abs)
# print(s_li)
# Remove the list elemnt and return it
# removed_fruits = fruits.pop()
# print(removed_fruits)
# print(fruits)

# Remove on a specific position
# removed_specific = fruits.pop(1)
# print(removed_specific)
# print(fruits)


# languages = ['Python', 'Go', 'Dart']
# for i in range(len(languages)):
#     print('#' + str(i + 1), languages[i])

# convert a user-entered string list to an integers list using maps

# a = input("Enter some numbers : ").strip().split(' ')
# a = list(map(int, a))  # int here is function not data type
# print(a)

# b = [1, 2, 3, 4]

# list1 = [1, 2, 3]
# list2 = list1

# list1[0] = 4
# print(list2)
# print(list1)

# def multiply_by_two(x):
#     return x * 2


# c = list(map(multiply_by_two, b))
# print(c)

# Filtering can be used to remove spacific items

# a = [1, 2, 3, 4, 5, 6, 7, 8]


# def is_even(x):
#     return x % 2 == 0


# a = list(filter(is_even, a))

# print(a)

# creat a list

# lists = [[]for i in range(3)]

# lists[0].append(3)
# lists[1].append(5)
# lists[2].append(7)
# print(lists)


####################################################


# list comprehensions!

# [print([i], end="")for i in fruits]

# for fruit in fruits:
#     fruit = fruit.upper()
#     new_fruits.append(fruit)

# fruits = new_fruits
# print(new_fruits)

# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

####################################################

# replace false with 0 and true with 1

# bits = ['False', 'True', 'True', 'False', 'False', 'True']
# new_bits = []

# for b in bits:
#     if b == 'True':
#         new_bits.append(1)
#     else:
#         new_bits.append(0)

# print(bits)
# print(new_bits)

# comperhansion_bits = [1 if b == 'True' else 0 for b in bits]

# print(comperhansion_bits)

####################################################

# when you see upper letter add space

# my_string = "HelloMyNameIsToqi"
# my_string = "".join([i if i.islower() else " " + i for i in my_string])[1:]# to remove the first space
# print(my_string)

##################################################

# squares = [x**2 for x in range(10)]
# print(squares)

# prackets = [[x, y] for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(prackets)

# print the number and its square

# num_square = [(x, x**2) for x in range(6)]
# print(num_square)

# vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# num = [num for elem in vec for num in elem]
# print(num)
##################################################
# generate list of all possible coordinates(i,j,k) where i+j+k not equal to n

# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# z = int(input("Enter z:"))
# n = int(input("Enter n: "))

# coordinates = [[i, j, k] for i in range(
#     x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
# print(coordinates)
################################################

# find the next grat number (find ruuner-up-score)
# if __name__ == '__main__':
#     n = int(input("Enter n: "))
#     arr = map(int, input("Enter list: ").split())

# # conver the map object to the list and remove duplivate
#     score = list(str(arr))

# # sort the list in descending order
#     sorted_scores = sorted(score, reverse=True)

# # the runner_up_score the scond great number
#     runner_up_score = sorted_scores[1]

#     print(runner_up_score)

import datetime
my_date = datetime.datetime(2023, 9, 9)
sentence = '{0: %B %d %Y} fell on a {0:%A} and was the {0:%j} daay of the year'.format(
    my_date)
print(sentence)
