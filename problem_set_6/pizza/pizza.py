import sys
import csv
from tabulate import tabulate

def check_command():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a csv file")

def main():
    check_command()

    csv_file = sys.argv[1]

    table = []

    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file)

        for line in csv_reader:
            table.append(line)

    print(tabulate(table[1:], headers = table[0], tablefmt="grid"))

if __name__ == "__main__":
    main()
