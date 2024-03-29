from cs50 import get_int

while True:
    card = get_int("Card: ")
    if card > 0:
        break


def luhn_checksum(card):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10


lenght = 0
visa = card
master = card
amex = card

length = len(str(card))

while visa >= 10:
    visa = int(visa / 10)

while amex >= 10**13:
    amex = int(amex / 10**13)

while master >= 10**14:
    master = int(master / 10**14)

if luhn_checksum(card) == 0:
    if visa == 4 and (length == 13 or length == 16):
        print("VISA")
    elif length == 15 and (amex == 34 or amex == 37):
        print("AMEX")
    elif length == 16 and (51 <= master <= 55):
        print("MASTERCARD")
    else:
        print("INVALID")
else:
    print("INVALID")


# #find the digits to be multiply by 2
# card1 = int(card % 10**2/10)*2
# card2 = int(card % 10**4 / 10**3)*2
# card3 = int(card % 10**6 / 10**5)*2
# card4 = int(card % 10**8 / 10**7)*2
# card5 = int(card % 10**10 / 10**9)*2
# card6 = int(card % 10**12 / 10**11)*2
# card7 = int(card % 10**14 / 10**13)*2
# card8 = int(card % 10**16 / 10**15)*2

# card1 =int(card % 100/10)* (card %10)
# card2 =int(card % 100/10)* (card2 %10)
# card3 =int(card % 100/10)* (card3 %10)
# card4 =int(card % 100/10)* (card4 %10)
# card5 =int(card % 100/10)* (card5 %10)
# card6 =int(card % 100/10)* (card6 %10)
# card7 =int(card % 100/10)* (card7 %10)
# card8 =int(card % 100/10)* (card8 %10)


# sum1 = card1 + card2 +card3 +card4 + card5 + card6 + card7 = card8

# #find digits not multiplied by 2

# card9 = int(card %10)
# card10 = int(card %10**3 / 10**2)
# card11 = int(card %10**5 / 10**4)
# card12 = int(card %10**7 / 10**6)
# card13 = int(card %10**9 / 10**8)
# card14 = int(card %10**11 / 10**10)
# card15 = int(card %10**13 / 10**12)
# card16 = int(card %10**15 / 10**14)

# sum2 = card9 + card10 + card11 + card12 + card13 + card14 + card15 + card16
