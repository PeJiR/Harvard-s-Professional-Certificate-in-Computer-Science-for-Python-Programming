def main():

    answer=input ("Greetings! ")
    output= value(answer)
    print(f"$ {output}")


def value(answer):
    answer = answer.lower().strip()
    #if answer has "Hello" output is 0$

    if "hello" in answer:
        return 0

    #if answer starts with "H" output is 20$

    elif "h" in answer:
        return 20

    #otherwise, output is 100$

    else:
        return 100


if __name__ == "__main__":
    main()

