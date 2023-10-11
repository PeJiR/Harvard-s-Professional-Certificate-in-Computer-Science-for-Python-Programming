menu ={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#set total amount to 0
total_amount = 0
while True:
#loop forever
    try:
        #get user input
        item = input("Item: ").title()
        #check if the item already exists in the dictonary
        if item in menu:
            #add the item price to total amount
            total_amount += menu[item]
            #print current total amount
            print("Total: $", end="")
            print("{:.2f}".format(total_amount))

    except EOFError:
        #print a new line and stop the loop
        print()
        break













