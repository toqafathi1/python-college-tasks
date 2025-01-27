
# 2- implement this program to handle numbers and special characters as well
def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr(
                    (ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr(
                    (ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_char = chr(
                (ord(char) - ord(' ') + shift) % 95 + ord(' '))
        ciphertext += encrypted_char
    return ciphertext


def caesar_decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr(
                    (ord(char) - ord('A') - key) % 26 + ord('A'))
            else:
                decrypted_char = chr(
                    (ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            decrypted_char = chr((ord(char) - ord(' ') - key) % 95 + ord(' '))
        decrypted_text += decrypted_char
    return decrypted_text


def get_shift_from_user():
    while True:
        try:
            shift = int(input("Enter the shift value: "))
            return shift
        except ValueError:
            print("Invalid input. Please enter an integer value.")


def get_message_from_user():
    message = input("Enter the message: ")
    return message


def get_operation_from_user():
    while True:
        operation = input(
            "Do you want to encrypt (E), decrypt (D), or exit (X)?: ").upper()
        if operation in ["E", "D", "X"]:
            return operation
        print("Invalid input. Please enter 'E' for encryption, 'D' for decryption, or 'X' to exit.")


while True:
    operation = get_operation_from_user()

    if operation == "X":
        print("Exiting the program.")
        break

    message = get_message_from_user()

    if operation == "E":
        shift = get_shift_from_user()
        result = caesar_encrypt(message, shift)
        print("Encrypted message:", result)
    elif operation == "D":
        key = get_shift_from_user()
        decrypted_message = caesar_decrypt(message, key)
        print("Decrypted message:", decrypted_message)
