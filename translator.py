
# vowel => a e i o u => relpce it with z

def translate(str):
    translation = ""
    for letter in str:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "Z"
            else:
                translation = translation + "z"

        else:
            translation = translation + letter
    return translation


print(translate(input("Enter the world ")))
