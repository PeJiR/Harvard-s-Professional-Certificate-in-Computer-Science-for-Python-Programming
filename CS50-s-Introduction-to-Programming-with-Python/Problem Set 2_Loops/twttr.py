def main():

    #get user input
    answer = input("Input: ")
    message_without_vowels= shorten(answer)
    #print output
    print("Output: " + message_without_vowels)

def shorten(answer):
    message_without_vowels= ""
    #loop through every letter
    for letter in answer:

        #check if it is a vowel or not
        if not letter.lower() in ['a','e','i','o','u']:
           message_without_vowels += letter

    return message_without_vowels

if __name__=="__main__":
    main()