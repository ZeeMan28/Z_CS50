menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

order = input("Item: ")
total = 0

while order != "control-d":
    order = order.title()

    if order in menu:
        total = float(total)
        total += menu[order]

    total = str(total)
    if len(total[total.find("."):]) < 2:
        total = total + "0"


    print("$" + str(total))

    order = input("Item: ")

print("$" + str(total))
