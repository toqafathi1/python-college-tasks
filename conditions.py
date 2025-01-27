
# score = int(input("Enter your score: "))

# if score >= 90:
#     print("Grade A: ")
# elif score >= 80:
#     print("Grade B: ")
# elif score >= 70:
#     print("Grade c:")
# elif score >= 60:
#     print("Grade D: ")
# else:
#     print("Grade f: ")

################################

# age = input("Enter your age: ").strip()

# unit = input("Enter time unit : Months ,Days ,weeks,").strip().lower()

# months = int(age) * 12
# weeks = months * 4
# days = int(age) * 365

# if unit == 'months':

#     print(f"your age is {months:,} month")

# elif unit == 'weeks':

#     print(f"your age is {weeks:,} week")

# elif unit == 'days':
#     print(f"your age is {days:,} day")

################################

# admins = ["Toqi", "Basma", "Rahma", "Esraa", "Eman"]

# yourName = input("Enter your name: ").strip().capitalize()

# if yourName in admins:
#     print(f"Hello,{yourName}")

#     option = input("Delete or Update :").strip().capitalize()

#     if option == 'Update':
#         theNewName = input("Enter your new name: ").strip().capitalize

#         admins[admins.index(yourName)] = theNewName

#         print("name Updated")

#         print(admins)
#     elif option == 'Delete':
#         admins.remove(yourName)
#         print("name Deleted")
#         print(admins)

#     else:
#         print("wrong option")

# else:

#     status = input("you are not admin , add you Y ,N ?").strip().capitalize()
#     if status == 'Yes' or status == 'Y':
#         print("you have been added ")
#         admins.append(yourName)

#         print(admins)
#     else:
#         print("you are not allowed ")
#########################################

# tries = 4
# mainPasswoed = "@toqi123"
# inputPasswoed = input("Enter your Password: ")
# while inputPasswoed != mainPasswoed:
#     tries -= 1

#     print(f"Wrong Password, {'last' if tries ==0 else tries } tries left")

#     inputPasswoed = input("Enter your Password: ")

#     if tries == 0:
#         print("Try again")
#         break
################################
