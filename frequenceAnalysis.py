
from collections import Counter

letters = "abcdefghijklmnopqrstuvwxyz "


def frequency_analysis(cipher_text):
    cipher_text = ''.join(char.lower()
                          for char in cipher_text if char.isalpha())
    letter_freq = {}

    for letter in letters:
        letter_freq[letter] = 0

    for letter in cipher_text:
        if letter in letters:
            letter_freq[letter] += 1

    counter = Counter(letter_freq)
    sorted_freq = counter.most_common()
    most_common_letter = sorted_freq[0][0]
    key = (ord(most_common_letter) - ord('e')) % 26

    return letter_freq, key


def decrypt_caesar(cipher_text, key):
    plain_text = []
    for letter in cipher_text.lower():
        if letter.isalpha():
            decrypted_letter = chr(
                (ord(letter) - key - ord('a')) % 26 + ord('a'))
            plain_text.append(decrypted_letter)
        else:
            plain_text.append(letter)

    return ''.join(plain_text)


# Example usage
cipher_text = "shuirup iuhtxhqfb dqdobvlv rq wkh surylghg flskhuwhaw. Lw zloo dvvxph wkdw wkh prvw frpprq ohwwhu lq wkh flskhuwhaw uhsuhvhqwv 'h' dqg fdofxodwh wkh nhb dffruglqjob. Wkh flskhuwhaw zloo eh ghfubswhg xvlqj wkh nhb, dqg zklwh vsdfhv zloo eh pdlqwdlqhg"

letter_freq, cracked_key = frequency_analysis(cipher_text)
plain_text = decrypt_caesar(cipher_text, cracked_key)

print("Letter Frequencies:", letter_freq)
print("Cracked Key:", cracked_key)
print("Decrypted Message:", plain_text)
