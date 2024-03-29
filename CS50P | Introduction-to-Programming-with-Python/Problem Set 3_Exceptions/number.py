# try:
#     x= int(input("What's x "))
#     print(f"x is {x}")

# except ValueError:
#     print("x is not an integer")


# def main():
#     x= get_in()
#     print(f"x is {x}")

# def get_in():
#     while True:
#         try:
#             return int(input("What's x "))

#         except ValueError:
#             print("x is not an integer")

#         # else:
#         #     return x
# main()


def main():
  x= get_in()
  print(f"x is {x}")

def get_in():
  while True:
    try:
      return int(input("What's x "))

    except ValueError:
      pass



main()








