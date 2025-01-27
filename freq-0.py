
def frequency_analysis(ciphertext):
    # Remove non-alphabetic characters and convert to lowercase
    ciphertext_f = ''.join(filter(str.isalpha, ciphertext)).lower()

    # Calculate the frequency of each letter in the ciphertext
    letter_frequency = {}
    for letter in ciphertext_f:
        if letter.isalpha():
            if letter in letter_frequency:
                letter_frequency[letter] += 1
            else:
                letter_frequency[letter] = 1

    # Sort the letters in descending order of frequency
    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)

    # Print the letter frequencies
    for letter, frequency in sorted_frequency:
        print(f"{letter}: {frequency}")

    # Prompt user for decryption guesses
    print("\nMake decryption guesses:")
    decryption_mapping = {}
    for letter in sorted_frequency:
        ciphertext_letter = letter[0]
        decrypted_letter = input(f"Replace '{ciphertext_letter}' with: ")
        decryption_mapping[ciphertext_letter] = decrypted_letter

    # Decrypt the ciphertext using the decryption mapping
    plaintext = ''
    for letter in ciphertext.lower():
        if letter.isalpha():
            decrypted_letter = decryption_mapping[letter]
            plaintext += decrypted_letter
        else:
            plaintext += letter

    return plaintext


# Example usage
ciphertext = "Wklv lv d vhfuhw phvvdjh, lw qhhgv wr kdyh pdqb uhshwlwlyh ohwwhuv lq rughu wr zrun"
plaintext = frequency_analysis(ciphertext)
print("\nDecrypted plaintext:", plaintext)