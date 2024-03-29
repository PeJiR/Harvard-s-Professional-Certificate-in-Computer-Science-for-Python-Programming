# make a dictionary that stores the shopping list

list = {}

# make a while loop that accepts items

while True:

    try:

        # ask for item

        item = input().upper()

        # see if item is in shopping list

        if item in list:

            list[item] = list[item] + 1

        # if item isnt

        else:

            list[item] = 1

    # once done with making shopping list

    except EOFError:

        for item in sorted(list):

            print(list[item], item)

        break


