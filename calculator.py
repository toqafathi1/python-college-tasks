
# make calculator for doing basic calculations

# def inputs():
#     first_number = int(input("Enter the first number:"))
#     second_number = int(input("Enter the second number:"))
#     operation = input("What operation to perform (+,-,/,*)? ")

#     if operation == "+":
#         print(f"the result= {first_number + second_number}")
#     elif operation == "-":
#         print(f"the result={first_number - second_number}")
#     elif operation == "/":
#         print(f"the result={first_number/second_number}")
#     elif operation == "*":
#         print(f"the result={first_number*second_number}")
#     else:
#         print(" you choose wrong operation.please choose (+,-,/,*)")


# def main():
#     inputs()

#     print("Thanks for using our calculator")


# main()

##################################################

# improved and faster  version for calculating

# def performe_operation(first_number, second_number, operation):
#     if operation == "+":
#         return first_number + second_number
#     elif operation == "-":
#         return first_number - second_number
#     elif operation == "*":
#         return first_number * second_number
#     elif operation == "/":
#         if second_number == 0:
#             print("Error: Can't divide by zero.")
#             return None
#         return first_number / second_number
#     else:
#         return None


# def calculation():
#     while True:
#         try:
#             first_number = float(input("Enter the First Number: "))
#             second_number = float(input("Enter the Second Number: "))
#             operation = input(
#                 "which operation you want to choose , (+, -, * ,/ )?")
#             result = performe_operation(first_number, second_number, operation)
#             if result is not None:
#                 print("The result is: ", result)
#             else:
#                 print("Invalid operation! choose from (+, -, *,/)")
#             choice = input(
#                 "Do you want to perform anthor operation? (yes or no)").lower().strip()
#             if choice == "no":
#                 break

#         except ValueError:
#             print("Invalid input. Please enter numeric values.")


# def main():
#     print("Welcome to the calculator")
#     calculation()
#     print("Thanks for using the calculator")


# if __name__ == "__main__":
#     main()

def main():
    print(square(2))


def square(n):
    return n*n


if __name__ == "__main__":
    main()
