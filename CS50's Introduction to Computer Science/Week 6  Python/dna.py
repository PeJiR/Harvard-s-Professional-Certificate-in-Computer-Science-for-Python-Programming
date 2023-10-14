from sys import argv
from cs50 import get_string

# TODO: Check for command-line usage
if len(argv) != 3:
    print("Error: Usage: python main.py database.csv dna.txt")
    exit(1)

# TODO: Read database file into a variable
csv_file = open(argv[1], "r")

strands = []
persons = {}
for ind, row in enumerate(csv_file):
    if ind == 0:
        strands = [strand for strand in row.strip().split(",")][1:]
    else:
        cur_row = row.strip().split(",")
        persons[cur_row[0]] = [int(x) for x in cur_row[1:]]

# TODO: Read DNA strand file into a variable
dna_strand = open(argv[2], "r").read()

# TODO: Find the maximum number of times each strand appears in the DNA strand
final_strands = []
for strand in strands:
    i = 0
    max_strand = -1
    cur_max = 0
    while i < len(dna_strand):
        cur_window = dna_strand[i : i + len(strand)]
        if cur_window == strand:
            cur_max += 1
            max_strand = max(max_strand, cur_max)
            i += len(strand)
        else:
            cur_max = 0  # reset my current max
            i += 1

    final_strands.append(max_strand)

# TODO: Find the person whose DNA strand matches the most strands in the DNA strand
for name, data in persons.items():
    if data == final_strands:
        print(name)
        break
else:
    print("No match")

# Print debug information
print(strands)
print(persons)
print(final_strands)
