

# # caesar cipher Encryption 1
# def caesar_encrypt(plainText, shift):
#     cipherText = ""
#     for char in plainText:
#         if char.isalpha():
#             ascii_offset = ord('A') if char.isupper() else ord('a')
#             encrypted_char = chr(
#                 (ord(char)-ascii_offset+shift) % 26 + ascii_offset)
#             cipherText += encrypted_char

#         else:
#             cipherText += char

#     return cipherText


# if __name__ == "__main__":
#     plainText = "This is a secret message"
#     shift = 3
#     cipherText = caesar_encrypt(plainText, shift)
#     print("cipherText: ", cipherText)

########################################################################

# def caesar_decrypt(ciphertext, key):
#     decrypted_text = ""
#     for char in ciphertext:
#         if char.isalpha():
#             ascii_offset = ord('A') if char.isupper() else ord('a')
#             decrypted_char = chr(
#                 (ord(char) - ascii_offset - key) % 26 + ascii_offset)
#             decrypted_text += decrypted_char
#         else:
#             decrypted_text += char
#     return decrypted_text


# def decrypt_with_unknown_key(ciphertext):
#     for key in range(26):  # Try all possible keys from 0 to 25
#         decrypted_message = caesar_decrypt(ciphertext, key)
#         print(f"Key {key}: {decrypted_message}")


# # Example usage
# ciphertext = "KHOOR"
# decrypt_with_unknown_key(ciphertext)

###############################################################################

# def caesar_encrypt(plaintext, key):
#     ciphertext = ""
#     for char in plaintext:
#         if char.isalpha():
#             ascii_offset = ord('A') if char.isupper() else ord('a')
#             encrypted_char = chr(
#                 (ord(char) - ascii_offset + key) % 26 + ascii_offset)
#             ciphertext += encrypted_char
#         else:
#             ciphertext += char
#     return ciphertext


# def caesar_decrypt(ciphertext, key):
#     decrypted_text = ""
#     for char in ciphertext:
#         if char.isalpha():
#             ascii_offset = ord('A') if char.isupper() else ord('a')
#             decrypted_char = chr(
#                 (ord(char) - ascii_offset - key) % 26 + ascii_offset)
#             decrypted_text += decrypted_char
#         else:
#             decrypted_text += char
#     return decrypted_text


# def decrypt_with_unknown_key(ciphertext):
#     for key in range(26):  # Try all possible keys from 0 to 25
#         decrypted_message = caesar_decrypt(ciphertext, key)
#         print(f"Key {key}: {decrypted_message}")


# # Input from the user
# user_message = input("Enter the message: ")
# user_key = int(input("Enter the key (an integer from 0 to 25): "))

# # Encrypt the user's message
# encrypted_message = caesar_encrypt(user_message, user_key)
# print("Encrypted message:", encrypted_message)

# # Decrypt the message with all possible keys
# decrypt_with_unknown_key(encrypted_message)

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
        operation = input(
            "Do you want to encrypt (E) or decrypt (D)?: ").upper()
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
###############################################
# 1- implement brute force to crack a code


def caesar_decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr(
                (ord(char)-ascii_offset - key) % 26 + ascii_offset)
            decrypted_text += decrypted_char

        else:
            decrypted_text += char

    return decrypted_text


def decrypt_with_unknown_key(ciphertext):
    for key in range(26):  # key 0 to 25
        decrypted_massage = caesar_decrypt(ciphertext, key)
        print(f"ket {key} : {decrypted_massage}")


ciphertext = "KHOOR"
decrypt_with_unknown_key(ciphertext)
