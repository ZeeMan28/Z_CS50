import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    letters = ""
    digits = ""
    punc = True
    j = 0

    zero = s.find("0")
    #for i in s[0:3:1]:
    # for i in s[::-1]
    for idx, i in enumerate(s):
        
        if i.isalpha():
            letters += i
            digits += " "
        else:
            digits += i
            letters += " "
            j += 1

        for q in string.punctuation:
            if q == i:
                punc = False


    if len(digits.strip()) == 0:
        digits = "1"


    if (s[0:2].isalpha()) and (2 <= len(s) <= 6) and (s[0:(len(s)-j)] == letters[0:len(s)-j]) and (digits.strip()[0] != "0") and (punc == True):
        return True
    else:
        return False


main()