import numpy as np
from egcd import egcd  # to find modular inverse of a metrix determinant

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

# mapping each letter to its index in alphabet
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def key_matrix_inv(key_matrix, modulus):  # modulus is lenght of alphabet 26

    determinant = int(np.round(np.linalg.det(key_matrix)))  # find determinant
    # to find the modular multiplicative inverse of the determinant
    determinant_inv = egcd(determinant, modulus)[1] % modulus

    key_matrix_inv = (
        determinant_inv *
        np.round(determinant * np.linalg.inv(key_matrix)).astype(int) % modulus
    )  # the modular inverse of the key matrix

    return key_matrix_inv


def encrypt(plain_text, K_matrix):
    cipher_text = ""
    message_in_numbers = []

    for letter in plain_text:
        message_in_numbers.append(letter_to_index[letter])

    split_ptext = [
        message_in_numbers[i: i + int(K_matrix.shape[0])]
        for i in range(0, len(message_in_numbers), int(K_matrix.shape[0]))
    ]  # splitting of the message_in_numbers into blocks of size K_matrix

    for block in split_ptext:
        # Convert the block to a column vector of numbers
        block = np.transpose(np.asarray(block))[:, np.newaxis]
        # add 'z' if there is mismatch size
        while block.shape[0] != K_matrix.shape[0]:
            block = np.append(block, letter_to_index["z"])[:, np.newaxis]
        # Multiply the key matrix with the block
        encrypted_numbers = np.dot(K_matrix, block) % len(alphabet)
        n = encrypted_numbers.shape[0]  # length of the encrypted message

        # Convert the encrypted numbers  back to a string
        for row in range(n):
            number = int(encrypted_numbers[row, 0])
            cipher_text += index_to_letter[number]

    return cipher_text


def decrypt(cipher_text, key_matrix_inv):
    plain_text = ""
    cipher_in_numbers = []

    for letter in cipher_text:
        cipher_in_numbers.append(letter_to_index[letter])

    split_CText = [
        cipher_in_numbers[i: i + int(key_matrix_inv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(key_matrix_inv.shape[0]))
    ]

    for C in split_CText:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(key_matrix_inv, C) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            plain_text += index_to_letter[number]

    return plain_text


def main():

    message = "Free Palestine"

    K_matrix = np.array([[3, 10, 20], [20, 19, 17], [23, 78, 17]])

    K_inv = key_matrix_inv(K_matrix, len(alphabet))

    cipher_text = encrypt(message, K_matrix)
    plain_text = decrypt(cipher_text, K_inv)

    print("Original message: " + message)
    print("Encrypted message: " + cipher_text)  # zeOBqwFmzHjsXtD
    print("Decrypted message: " + plain_text)  # Free Palestinez


main()
