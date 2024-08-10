due = 50


while due > 0:
    print("Amount Due: " + str(due))

    answer = input("Insert Coin: ")

    match answer:
        case "5" | "10" | "25":
            due -= int(answer)

if due < 0:
    print("Change Owed: " + str(due*-1))

if due == 0:
    print("Change Owed: 0")
