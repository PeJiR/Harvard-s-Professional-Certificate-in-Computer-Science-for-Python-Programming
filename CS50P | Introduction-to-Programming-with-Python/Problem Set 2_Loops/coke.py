coke_price = 50

while coke_price > 0:
    print("Amount Due: " + str(coke_price))
    insert_coin = int(input("Insert Coin: "))

    if insert_coin in [5,10,25]:
            coke_price -= insert_coin
    else:
        print("Invalid coin! Please insert 5,10, or 25 cents")

print("Change Owed: " + str(-coke_price))
