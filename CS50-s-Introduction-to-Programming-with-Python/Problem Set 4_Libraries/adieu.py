import inflect

p = inflect.engine()

#Create a list to keep track of names
names = []

#loop forever
while True:
    try:
    #ger user input
        name =input("Name: ")
        names.append(name)

    except EOFError:
        print()
        break

#printing using inflect

output = p.join(names)
print("Adieu, adieu, to " + output)

