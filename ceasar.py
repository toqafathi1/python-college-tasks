# # ###########  implemintation 1 ###########

def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset) #get it back to ascii so tthat we can use the function chr
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

# Example usage
plaintext = "This is a secret message"
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)

print("Ciphertext:", ciphertext)







# 65 66 67 68 69
# 0  1  2  3  4
# A  B  C  D  E
# D  E  F  G  H

'''
(ord(char) - ascii_offset + shift) calculates the shifted position of the character relative to the starting point ('A' or 'a').

% 26 performs the modulo operation with 26, which means dividing the value by 26 and taking the remainder. This operation ensures that the result falls within the range of 0-25.

For example, let's consider the lowercase letter 'x' with an ASCII value of 120:

ord(char) returns 120.
ascii_offset for lowercase letters is 97 ('a').
So, ord(char) - ascii_offset + shift becomes 120 - 97 + 3 = 26.
Then, (ord(char) - ascii_offset + shift) % 26 is 26 % 26, which is equal to 0.
By taking the remainder modulo 26, we wrap the result back into the range of 0-25. This allows us to map the shifted position back to the corresponding letter in the alphabet.
'''

########## implemintation 2 #########
def caesar_encrypt(plaintext, shift):
    ciphertext = [chr((ord(char) - 65 + shift) % 26 + 65) if 'A' <= char <= 'Z' else
                  chr((ord(char) - 97 + shift) % 26 + 97) if 'a' <= char <= 'z' else char
                  for char in plaintext]
    return ''.join(ciphertext)

plaintext = "This is a secret message"
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)

print("Ciphertext:", ciphertext)

'''In this implementation, a list comprehension is used to iterate over each character in the plaintext. The ord(char) function is used to get the ASCII value of the character.

For uppercase letters ('A' to 'Z'), the character is shifted by subtracting 65 ('A') to normalize it to the range of 0-25. The modulo operation % 26 ensures that the value wraps within the range. Finally, the result is converted back to a character using chr() and added to the ciphertext list.

For lowercase letters ('a' to 'z'), a similar process is followed, but we subtract 97 ('a') instead.

If the character is not an alphabetical letter, it is directly added to the ciphertext list without any modification.

Finally, the ciphertext list is joined using ''.join(ciphertext) to obtain the encrypted message as a string.
'''




########## implemintation 3 ############
def caesar_encrypt(plaintext, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char_index = alphabet.find(char.lower())
            encrypted_index = (char_index + shift) % 26
            encrypted_char = alphabet[encrypted_index]
            if is_upper:
                encrypted_char = encrypted_char.upper()
        else:
            encrypted_char = char
        ciphertext += encrypted_char
    return ciphertext

def caesar_decrypt(ciphertext, key):
    shift = -key if key else 0  # Negative shift for decryption
    return caesar_encrypt(ciphertext, shift)

plaintext = "This is a secRet message"
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)

print("Ciphertext:", ciphertext)

#The is_upper flag is used to determine whether the original character was uppercase or not, so we can preserve its case in the encrypted result.