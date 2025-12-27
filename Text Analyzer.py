text = input("Enter words or a sentence: ")

letters = 0
numbers = 0
letter_count = {}

for char in text:
    if char.isalpha():
        letters += 1
        char = char.lower()   # make it case-insensitive
        letter_count[char] = letter_count.get(char, 0) + 1
    elif char.isdigit():
        numbers += 1

print("Total letters:", letters)
print("Total numbers:", numbers)

print("\nRepeated letters:")
for letter, count in letter_count.items():
    if count > 1:
        print(letter, "=", count)