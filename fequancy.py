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
    
    print(f"Key: {key}")

    # Decrypt the ciphertext using the guessed key
    decrypted_text = []
    for letter in ciphertext.lower():
        if letter.isalpha():
            decrypted_letter = chr((ord(letter) - key - ord('a')) % 26 + ord('a'))
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
print("Decrypted plaintext:", plaintext)
