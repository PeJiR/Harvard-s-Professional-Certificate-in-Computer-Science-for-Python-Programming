from cs50 import get_string

text = get_string("Text: ")

letters = sentences = words = 0

for char in text:
    if char.isalpha():
        letters += 1
    if char.isspace():
        words += 1
    if char in ("?", ".", "!"):
        sentences += 1

words +=1
L = (letters * 100) / words
S = (sentences * 100) / words
result = int((0.0588 * L - 0.296 * S - 15.8) + 0.5)
result = round(result)


if result > 16:
    print("Grade 16+")
elif result > 1 and result < 17:
    print(f"Grade {result}")
else:
    print("Before Grade 1")
