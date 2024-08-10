

def main():
    gas = "wrong"

    while gas == "wrong":
        gas = input("Fraction: ")
        gas = gauge(convert(gas))

    print(gas)


def convert(t):
    t = t.strip()

    #making sure both ints are numbers
    if (not t[:t.find("/")].isdigit()) or (not t[(t.find("/") + 1):].isdigit()):
        return "wrong"

    else:
        first = int(t[:t.find("/")])
        second = int(t[(t.find("/") + 1):])

        if (second == 0) or (first > second):
            return "wrong"
        # elif round(first / second, 2) * 100 >= 99:
        #     return "F"
        # elif round(first / second, 2) * 100 <= 1:
        #     return "E"
        else:
            final = str((round(first / second, 2) * 100))

            return int(final[:final.find(".")])

def gauge(x):
    if x >= 99:
        return "F"
    elif x <= 1:
        return "E"
    else:
        return str(x) + "%"


if __name__ == "__main__":
    main()
