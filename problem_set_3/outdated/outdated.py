
month_bank = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

valid = False

def main():
    while valid == False:
        try:
            date = input("Date: ")

            date = convert(date)

            if date != "bad":
                break

        except EOFError:
            break

    print(date)

def convert(q):
    q = q.title().strip()


    year = q[-4:]
    final_date = year + "-"

    if " " in q and "," in q:
        q = q.split(" ")

        if q[0] in month_bank:

            #assign month
            month = month_bank.index(q[0]) + 1
            if month < 10:
                month = "0" + str(month)

            if int(q[1][:-1]) > 31:
                return "bad"

            #assign day
            if int(q[1][:-1]) < 10:
                day = "0" + q[1][:-1]
            else:
                day = q[1][:-1]

        else:
            return "bad"


    elif "/" in q:
        q = q.strip()
        q_list = q.split("/")

        q = q.replace("/", "")

        if not q.isnumeric():
            return "bad"

        if int(q_list[1]) > 31:
            return "bad"
        elif int(q_list[0]) < 10:
            month = "0" + q_list[0]
        elif int(q_list[0]) > 12:
            return "bad"
        else:
            month = q_list[0]

        if int(q_list[1]) < 10:
            day = "0" + q_list[1]
        else:
            day = q_list[1]

    else:
        return "bad"


    valid = True
    final_date += str(month) + "-" + str(day)
    return final_date

main()
