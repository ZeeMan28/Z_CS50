def main():
    answer = input("Input: ")
    answer = shorten(answer)
    print(answer)


def shorten(word):

    new_word = ""

    for i in word:
        if not i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            new_word += i

    return new_word

if __name__ == "__main__":
    main()


