# encryption: c=(p+k)mod26
# decryption: p=(c-k)mod26
# This function generates the key in a cyclic manner until its length isn't equal to the length of the original text
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)])
    return ''.join(key)

# This function returns the encrypted text generated with the help of the key
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        if string[i].isalpha():
            is_upper = string[i].isupper()
            x = (ord(string[i].upper()) + ord(key[i].upper())) % 26
            x += ord('A' if is_upper else 'a')
            cipher_text.append(chr(x))
        else:
            cipher_text.append(string[i])
    return ''.join(cipher_text)

# This function decrypts the encrypted text and returns the original text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            is_upper = cipher_text[i].isupper()
            x = (ord(cipher_text[i].upper()) - ord(key[i].upper()) + 26) % 26
            x += ord('A' if is_upper else 'a')
            orig_text.append(chr(x))
        else:
            orig_text.append(cipher_text[i])
    return ''.join(orig_text)


string = "We are discovered SAVE YOURSELF"
keyword = "Key"
key = generateKey(string, keyword)
cipher_text = cipherText(string, key)
print("Ciphertext:", cipher_text)
print("PlainText:", originalText(cipher_text, key))
####
# print(ord('W'), ord('K'))
# print((ord('W')+ord('K'))%26)
# chrc=ord('A')+6
# print(chr(chrc))