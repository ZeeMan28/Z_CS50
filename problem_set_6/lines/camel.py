t = 0
k = 0
capitals = []

answer = input("camelCase: ")
     

for i in answer:
    t += 1
    if i.isupper() == True:
        capitals.append(t)

answer = answer.lower()

if len(capitals) > 0:
    for x in capitals:
        answer = answer[:x-1+k] + "_" + answer[x-1+k:]
        k += 1

print(answer)

