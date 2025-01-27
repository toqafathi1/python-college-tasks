
# Toqi fathi el_sayed

sentence = "Hello depp learning"

#  dictionary to store character counts
char_count = {}

# Iterate through the sentence
for char in sentence:
    # Convert the character to lowercase to ignore case sensitivity
    char = char.lower()

    # If the character is already in the dictionary, increment the count
    if char in char_count:
        char_count[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        char_count[char] = 1

# Print the character counts
for char, count in char_count.items():
    print(f"{char}: {count} ", end=" ")
