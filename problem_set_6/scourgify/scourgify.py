import sys
import csv

def check_command():
    if not len(sys.argv) == 3:
        sys.exit("need two command line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a csv file")

def main():
    check_command()

    try:
        csv_file = sys.argv[1]
        with open(csv_file, "r") as file:
            csv_reader = csv.reader(file)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
