

# secretWorld = "easy world"
# guess = ""

# guess_count = 0
# guess_limit = 3
# out_of_guess = False


# while guess != secretWorld and not out_of_guess:
#     if guess_count < guess_limit:

#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guess = True

# if out_of_guess:
#     print("you lose try again")

# else:
#     print("you win")

# #############################################

# fruit guessing game

# import random

# fruits = {"apple": {"description": "It is a round fruit with red, green , or yellow skin. ", "hints": ["It can be used to make apie .", "It is a popular snak"]},
#           "banana": {"description": "It is long , curved fruit with yellow skin. ", "hints": ["It is high in potassium.", "Monkes love this fruit."]},
#           "orange": {"description": "It is a citrus fruit with a bright orange skin.", "hints": ["It is a good source of vitamin C.", "It is commonly used to make juice."]},
#           "pear": {"description": "It is a sweet and juicy fruit with a narrow top and wider bottom.", "hints": ["It has a green or yellow skin.", "It is often eaten fresh."]},
#           "grape": {"description": "It is a small, round fruit that grows in clusters.", "hints": ["It can be purple, green, or red.", "It is used to make wine."]}
#           }

# max_attempts = 4


# def play_game():
#     random_fruit = random.choice(list(fruits.keys()))
#     attempts = 0

#     print("Welcome to the Guess the fruit game !")
#     print("you have ", max_attempts, "tries to guess the fruit.")
#     print(fruits[random_fruit]["description"])

#     while attempts < max_attempts:
#         guess = input("Enter your guess: ").lower().strip()

#         if guess == random_fruit:
#             print("Congratulations! You guessed the fruit correctly.")
#             return

#         print("Wrong guess! Try again.")
#         attempts += 1

#         if attempts < max_attempts:
#             hint = random.choice(fruits[random_fruit]["hints"])
#             print("Hints: ",  hint)

#     print("Sorry, you ran out of attempts. the fruit was ", random_fruit)


# def play_again():
#     while True:
#         choice = input(
#             "Do you wnant to  play again? (yes/no): ").lower().strip()
#         if choice == "yes":
#             return True
#         elif choice == "no":
#             return False
#         else:
#             print("Invalid input. please enter 'yes' or 'no'.")


# def main():
#     play_game()
#     while play_again():
#         play_game()
#     print("Thank you for playing the Guess the Fruit game!")


# main()

################################################################

# Number Guessing Game

# import random

# # print(dir(random))


# max_attempts = 4


# def play_game():
#     random_number = random.randint(1, 1000)
#     attempts = 0

#     print("Welcome to Guess the Number Game!")
#     print(f"you have {max_attempts} tries to guess Number  between 1 to 1000 ")

#     while attempts < max_attempts:
#         guess = int(input("Enter your guess: "))

#         if guess == random_number:
#             print("Congratulations! you guessed the Number correctly")
#             return

#         print("Worng Guess! Try again ")
#         attempts += 1

#         if attempts < max_attempts:
#             if guess > random_number:
#                 print("Your guess is too high ")
#             else:
#                 print("Your guess is too low.")

#     print("Sorry you are run out of tries.the Number was", random_number)


# def play_again():
#     while True:
#         choice = input("Do you want to play again?(yes/no): ")
#         if choice == "yes":
#             return True
#         elif choice == "no":
#             return False
#         else:
#             print("Invalid choice, Please choice 'yes' or 'no")


# def main():
#     play_game()
#     while play_again():
#         play_game()
#     print("Thanks for playing the Guess Number game .")


# main()

# make the comouter to guess the number
import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(
            f'Is {guess} too high(H),too low (L), or correct(C)??').lower()

        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    print(f'Yay! The Computer guessed your number ,{guess}, correctly!')


computer_guess(100)
