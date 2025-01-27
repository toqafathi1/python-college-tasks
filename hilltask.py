import numpy as np

# Substitution dictionary for mapping letters to numbers
substitution = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
               'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
               'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

# Inverse substitution dictionary for mapping numbers to letters
inverse_substitution = {value: key for key, value in substitution.items()}

def encrypt(plain_text, key_matrix):
    # Convert the plain text to uppercase
    plain_text = plain_text.upper()

    # Remove any spaces from the plain text
    plain_text = plain_text.replace(" ", "")

    # Pad the plain text if its length is not a multiple of the key matrix size
    if len(plain_text) % len(key_matrix) != 0:
        padding_length = len(key_matrix) - (len(plain_text) % len(key_matrix))
        plain_text += 'Z' * padding_length

    # Initialize the cipher text
    cipher_text = ''

    # Encrypt the plain text
    for i in range(0, len(plain_text), len(key_matrix)):
        # Get the current block of the plain text
        block = plain_text[i:i+len(key_matrix)]

        # Convert the block to a column vector of numbers
        block_vector = np.array([substitution[ch] for ch in block])

        # Multiply the key matrix with the block vector
        encrypted_vector = np.dot(key_matrix, block_vector) % 26

        # Convert the encrypted vector back to a string
        encrypted_block = ''.join([inverse_substitution[num] for num in encrypted_vector])

        # Append the encrypted block to the cipher text
        cipher_text += encrypted_block

    return cipher_text

def decrypt(cipher_text, key_matrix):
    # Initialize the decrypted text
    decrypted_text = ''

    # Invert the key matrix
    inverse_key_matrix = np.linalg.inv(key_matrix)

    # Calculate the determinant of the key matrix
    determinant = int(round(np.linalg.det(key_matrix)))

    # Calculate the modular inverse of the determinant
    modular_inverse = pow(determinant, -1, 26)

    # Iterate over the cipher text in blocks
    for i in range(0, len(cipher_text), len(key_matrix)):
        # Get the current block of the cipher text
        block = cipher_text[i:i+len(key_matrix)]

        # Convert the block to a column vector of numbers
        block_vector = np.array([substitution[ch] for ch in block])

        # Calculate the product of the inverse key matrix and the block vector
        decrypted_vector = (modular_inverse * np.dot(inverse_key_matrix, block_vector)) % 26

        # Convert the decrypted vector back to a string
        decrypted_block = ''.join([inverse_substitution[int(num)] for num in decrypted_vector])

        # Append the decrypted block to the decrypted text
        decrypted_text += decrypted_block

    return decrypted_text

# Example usage with the specified plain text
choice = input("Enter 'E' for encryption or 'D' for decryption: ")

if choice.upper() == 'E':
    plain_text = 'HOWIMETYOURMOTHER'
    key_matrix = np.array([[6, 24, 7], [1, 13, 6], [6, 24, 7]])
    cipher_text = encrypt(plain_text, key_matrix)
    print("Cipher Text:", cipher_text)
elif choice.upper() == 'D':
    cipher_text = 'VLNPUXFEKYYJ'
    key_matrix = np.array([[6, 24, 7], [1, 13, 6], [6, 24, 7]])
    decrypted_text = decrypt(cipher_text, key_matrix)
    print("Decrypted Text:", decrypted_text)
else:
    print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
