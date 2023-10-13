def main():
    plate = input("Plates: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    for c in s:
        if c == "0":
            return False

    i = 0
    while i < len(s):
        if not s[i].isalpha():
            break
        i += 1
    else:
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    invalid_characters = [".", " ", "?", "!"]
    for c in s:
        if c in invalid_characters:
            return False

    return True

if __name__ == "__main__":
    main()
