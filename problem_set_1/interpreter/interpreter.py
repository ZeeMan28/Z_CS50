problem = input("enter math problem: ")

a = int(problem[0:(problem.find(" "))])
b = problem[problem.find(" ")+1]
c = int(problem[problem.rfind(" ") + 1:])

match b:
    case "+":
        output = a + c
    case "-":
        output = a - c
    case "*":
        output = a * c
    case "/":
        output = a / c
    case _:
        print("penis")

print(float(output))