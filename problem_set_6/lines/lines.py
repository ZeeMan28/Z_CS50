import sys

def check_command():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def main():

    check_command()

    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()

    except FileNotFoundError:
        sys.exit("File does not exist")

#     stripped_lines = []
#     for i in lines:
#         #i = i.lstrip()
#         if not (i.lstrip() == "\n" or i.lstrip().startswith("#")):
#             stripped_lines.append(i)
# #
#     print(len(stripped_lines))

    bad_line_cnt = 0
    for i in lines:
        if i == "\n":
            bad_line_cnt += 1
            continue
        if  i.lstrip().startswith("#"):
            bad_line_cnt += 1
            continue
        if i.count(" ") == len(i)-1:
            bad_line_cnt += 1
            continue

    print(len(lines) - bad_line_cnt)



if __name__ == "__main__":
    main()
