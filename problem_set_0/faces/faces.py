
def convert(happy):
    print(f"happy = {happy}")
    newstr = happy.replace(":)", "🙂")
    newstr = newstr.replace(":(", "🙁")
    return newstr

def main():
    string = input("enter text here: ")
    string = convert(string)
    print(string)

main()