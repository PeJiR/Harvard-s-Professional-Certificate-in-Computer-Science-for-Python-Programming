import sys
import csv
from tabulate import tabulate

def main():
    check_command_line_arg()
    table = []

    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
        print(tabulate(table[1:],headers= table[0], tablefmt ="grid"))

    except FileNotFoundError:
        sys.exit ("File does not exit")


def check_command_line_arg():
    if len(sys.argv)<2:
        sys.exit ("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit ("Too many command-line arguments")

    if ".csv" not in sys.argv[1]:
        sys.exit("This is not a CSV file")






if __name__ == "__main__":
    main()
