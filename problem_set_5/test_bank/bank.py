
def main():
    greeting = input("Greeting: ").lower()
    greeting = greeting.replace(" ", "")

    greeting = value(greeting)
    print("$", str(greeting))


def value(z):
    if z[0:5] == "hello":
        value = 0
    elif z[0] == "h":
        value = 20
    else:
        value = 100

    return value


if __name__ == "__main__":
    main()
