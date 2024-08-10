z = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").lower()

z = z.replace(" ", "")
z = z.replace("yt", "y t")

if z == "42" or z == " 42 " or z == "forty two" or z == "forty-two":
    print("yes")
else:
    print("no")