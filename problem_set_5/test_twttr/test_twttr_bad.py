import twttr
import random

short_names = []

def main():
    names = generate_names

    names = test_no_vowels(names)

    print(names)


def generate_names():
    letters = "abcdefghijklmnopqrstuvwxyz"

    return_name = []

    for a in range(5):
        length = random.randint(2, 6)
        name = ""
        new_name = ""

        for i in range(length):
            name += letters[random.randint(0, 25)]

        for j in name:
            if random.random() < 0.5:
                new_name += j.upper()
            else:
                new_name += j

        return_name.append(new_name)

    return return_name



def test_no_vowels(long_names):

    long_names = generate_names()

    for q in long_names:
        short_names.append(twttr.shorten(q))

    return short_names



main()

