def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_char = char
        ciphertext += encrypted_char
    return ciphertext

def caesar_decrypt(ciphertext, key):
    shift = -key if key else 0  # Negative shift for decryption
    return caesar_encrypt(ciphertext, shift)

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
        operation = input("Do you want to encrypt (E) or decrypt (D)?: ").upper()
        if operation == "E" or operation == "D":
            return operation
        print("Invalid input. Please enter 'E' for encryption or 'D' for decryption.")

operation = get_operation_from_user()
message = get_message_from_user()

if operation == "E":
    shift = get_shift_from_user()
    result = caesar_encrypt(message, shift)
    print("Encrypted message:", result)
elif operation == "D":
    key = get_shift_from_user()
    result = caesar_decrypt(message, key)
    print("Decrypted message:", result)

############ TASK #########
# 1- implement brute force to crack a code
# 2- implement this program to handle numbers and special characters as well