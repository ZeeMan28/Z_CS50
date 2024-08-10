import inflect

names = []


while True:
        try:
            current_name = input("Name: ")

            names.append(current_name)

        except EOFError:
            break

print()


print("Adieu, adieu, to ", end="")

if len(names) == 2:
    print(names[0] + " and " + names[1])

elif len(names) > 2:

    for i in range(len(names) - 1):
         print(names[i] + ", ", end="")

    print("and " + names[-1])

else:
     print(names[0])



