groceries = {}
groceries_sorted = {}


while True:
    try:
        order = input()

        order = order.title()

        if order in groceries:
            groceries[order] += 1
        else:
            groceries[order] = 1

    except EOFError:
        break

keys = list(groceries.keys())
keys.sort()


for  k in keys:
    groceries_sorted[k] = groceries[k]


for i in groceries_sorted.keys():
    print(str(groceries_sorted[i]) + " " + i.upper())

