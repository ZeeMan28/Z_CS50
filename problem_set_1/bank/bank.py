z = input("Greeting: ").lower()
z = z.replace(" ", "")

if z[0:5] == "hello":
    print("$0")
elif z[0] == "h":
    print("$20")
else:
    print("$100")