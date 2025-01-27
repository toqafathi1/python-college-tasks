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
