import collections


def frequency_analysis(ciphertext):
    # Remove non-alphabetic characters and convert to lowercase
    ciphertext_filtered = ''.join(filter(str.isalpha, ciphertext)).lower()

    # Calculate the frequency of each letter in the ciphertext
    letter_frequency = collections.Counter(ciphertext_filtered)

    # Sort the letters in descending order of frequency
    sorted_frequency = letter_frequency.most_common()

    # Guess the most common letter in the ciphertext (assuming it represents 'e')
    most_common_letter = sorted_frequency[0][0]
    key = ord(most_common_letter) - ord('e')
    print('key: ', key)
    # Decrypt the ciphertext using the guessed key
    decrypted_text = []
    for letter in ciphertext.lower():
        if letter.isalpha():
            decrypted_letter = chr(
                (ord(letter) - key - ord('a')) % 26 + ord('a'))
            decrypted_text.append(decrypted_letter)
        else:
            decrypted_text.append(letter)

    # Generate text-based histogram of letter frequencies
    print("Letter Frequency Analysis:")
    for letter, frequency in sorted_frequency:
        bar = frequency
        print(f"{letter}: {bar}")

    return ''.join(decrypted_text)


# Example usage
ciphertext = "Qrz, zkhq brx uxq wklv frgh, lw zloo shuirup iuhtxhqfb dqdobvlv rq wkh surylghg flskhuwhaw. Lw zloo dvvxph wkdw wkh prvw frpprq ohwwhu lq wkh flskhuwhaw uhsuhvhqwv 'h' dqg fdofxodwh wkh nhb dffruglqjob. Wkh flskhuwhaw zloo eh ghfubswhg xvlqj wkh nhb, dqg zklwh vsdfhv zloo eh pdlqwdlqhg"
plaintext = frequency_analysis(ciphertext)
print("Decrypted plaintext 1:", plaintext)


# ciphertext1 = "Wklv lv d vhfuhw phvvdjh, lw qhhgv wr kdyh pdqb uhshwlwlyh ohwwhuv lq rughu wr zrun"
# plaintext1 = frequency_analysis(ciphertext1)
# print("Decrypted plaintext 2:", plaintext1)

# ciphertext2 = "Wklv lv d vhfuhw phvvdjh"
# plaintext2 = frequency_analysis(ciphertext2)
# print("Decrypted plaintext 3:", plaintext2)

'''
import collections: This line imports the collections module from the Python standard library. The collections module provides various specialized container datatypes, and in this case, we use the Counter class from collections to count the frequency of letters in the ciphertext.

def frequency_analysis(ciphertext): This line defines a function called frequency_analysis that takes a ciphertext as input. The function performs the frequency analysis and returns the decrypted plaintext.

ciphertext_filtered = ''.join(filter(str.isalpha, ciphertext)).lower(): This line removes non-alphabetic characters from the ciphertext and converts it to lowercase. The filter function is used to remove non-alphabetic characters, and str.isalpha is a method that checks if a character is a letter. The resulting filtered ciphertext is stored in the ciphertext_filtered variable.

letter_frequency = collections.Counter(ciphertext_filtered): This line creates a Counter object called letter_frequency that counts the frequency of each letter in the ciphertext_filtered.

sorted_frequency = letter_frequency.most_common(): This line sorts the letters in the letter_frequency counter in descending order of frequency, resulting in a list of tuples where each tuple contains a letter and its frequency.

most_common_letter = sorted_frequency[0][0]: This line extracts the most common letter from the sorted_frequency list. It assumes that the most common letter represents the letter 'e' in the English language.

key = ord(most_common_letter) - ord('e'): This line calculates the key used for decryption by finding the difference between the Unicode code point of the most common letter and the Unicode code point of 'e'. The assumption is that the key is the same for all letters.

decrypted_text = []: This line initializes an empty list to store the decrypted text.

The following lines iterate over each character in the ciphertext:

if letter.isalpha(): checks if the character is a letter.
decrypted_letter = chr((ord(letter) - key - ord('a')) % 26 + ord('a')) decrypts the letter by subtracting the key and converting it back to its corresponding Unicode code point. The modulo operator % is used to wrap around the alphabet if the result goes beyond 'z'.
decrypted_text.append(decrypted_letter) adds the decrypted letter to the decrypted_text list.
else: handles non-alphabetic characters and appends them as they are to the decrypted_text list.
return ''.join(decrypted_text): This line joins all the characters in the decrypted_text list into a single string and returns the decrypted plaintext.

The script provides example usage by decrypting three ciphertexts (ciphertext, ciphertext1, and ciphertext2) using the frequency_analysis function and printing the decrypted plaintext.

The frequency analysis technique assumes that the most frequent letter in the ciphertext corresponds to the letter 'e' in the English language. It calculates the key by finding the difference between the most common letter and 'e' and uses that key to decrypt the ciphertext. However, this technique may not always work if the ciphertext has a significantly different letter frequency distribution or if the key is not a simple shift cipher.
'''
