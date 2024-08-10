import random


def main():
    level = get_level()
    result = 10

    #generate problems
    problems = []
    for i in range(10):
        problems.append(str(generate_integer(level)) + " + " + str(generate_integer(level)))

    #present problems
    for i  in range(10):

        answer = input(problems[i] + " = ")
        actual_answer = int(problems[i][0:level]) + int(problems[i][len(problems[i]) - level:])

        tries = 1
        while int(answer) != actual_answer and tries < 3:
            print("EEE")
            answer = input(problems[i] + " = ")
            tries += 1

        if tries == 3:
            print(problems[i] + " = " + str(actual_answer))
            result -= 1

    print(result)



def get_level():

    getlevel = input("Level: ")

    while True:
        if not getlevel.isdigit():
            getlevel = input("Level: ")
        elif not 0 < int(getlevel) < 4:
            getlevel = input("Level: ")
        else:
            return int(getlevel)

    return getlevel


def generate_integer(q):

    if q == 1:
        return random.randint(0, 9)

    lower_bound = 10 ** (int(q) - 1)
    upper_bound = (10 ** int(q)) - 1

    integer = random.randint(lower_bound, upper_bound)

    return integer


if __name__ == "__main__":
    main()
