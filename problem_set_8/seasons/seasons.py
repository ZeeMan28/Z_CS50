from datetime import datetime
import re
import sys
import inflect

p = inflect.engine()

def main():
    birth = input("Date of Birth: ")

    given_date_str = test_date(birth)

    final_minutes = get_minutes(given_date_str)

    print(f"{final_minutes} minutes")

def get_minutes(q):
    current_date = datetime.today()
    given_date = datetime.strptime(q, "%Y-%m-%d")
    duration = current_date - given_date
    duration_minutes = duration.days * 1440

    return p.number_to_words(duration_minutes)

def test_date(birth):
    if not re.search(r"^\d{4}-\d{2}-\d{2}$", birth):
        sys.exit("Invalid date")
    else:
        return(birth)


if __name__ == "__main__":
    main()
