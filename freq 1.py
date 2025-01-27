def frequency_analysis(ciphertext):
    # Remove non-alphabetic characters and convert to lowercase
    ciphertext_filtered = ''.join(filter(str.isalpha, ciphertext)).lower()

    # Calculate the frequency of each letter in the ciphertext
    letter_frequency = {}
    for letter in ciphertext_filtered:
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1

    # Sort the letters in descending order of frequency
    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)

    # Guess the most common letter in the ciphertext (assuming it represents 'e')
    most_common_letter = sorted_frequency[0][0]
    key = ord(most_common_letter) - ord('e')
    print('key: ',key)
    # Decrypt the ciphertext using the guessed key
    decrypted_text = []
    for letter in ciphertext.lower():
        if letter.isalpha():
            decrypted_letter = chr((ord(letter) - key - ord('a')) % 26 + ord('a'))
            decrypted_text.append(decrypted_letter)
        else:
            decrypted_text.append(letter)
    
    decrypted_text = ''.join(decrypted_text)

    # Generate text-based histogram of letter frequencies
    print("Letter Frequency Analysis:")
    for letter, frequency in sorted_frequency:
        bar = '#' * frequency
        print(f"{letter}: {bar}")

    return decrypted_text

# Example usage


ciphertext = "Qrz, zkhq brx uxq wklv frgh"
plaintext = frequency_analysis(ciphertext)


print("Decrypted plaintext 1:", plaintext)
