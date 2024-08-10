

def main():
    gas = "wrong"

    while gas == "wrong":
        gas = input("Fraction: ")
        gas = convert(gas)

    gas = gauge(gas)

    print(gas)


def convert(t):
    t = t.strip()

    try:
        first = int(t[:t.find("/")])
        second = int(t[(t.find("/") + 1):])

        if (first > second):
            return "wrong"

        else:
            final = str((round(first / second, 2) * 100))

            return int(final[:final.find(".")])

    except ValueError:
        return "wrong"
    except ZeroDivisionError:
        return "wrong"



def gauge(x):
    if x >= 99:
        return "F"
    elif x <= 1:
        return "E"
    else:
        return str(x) + "%"


if __name__ == "__main__":
    main()
