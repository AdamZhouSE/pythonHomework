roma = list(input())
for i in range(len(roma)):
    r = roma[i]
    if r == "I":
        roma[i] = 1
    elif r == "V":
        roma[i] = 5
    elif r == "X":
        roma[i] = 10
    elif r == "L":
        roma[i] = 50
    elif r == "C":
        roma[i] = 100
    elif r == "D":
        roma[i] = 500
    else:
        roma[i] = 1000
number = 0
posi = 0
while posi < len(roma):
    if posi < len(roma)-1:
        if roma[posi] < roma[posi+1]:
            number += roma[posi+1]-roma[posi]
            posi += 2
        else:
            number += roma[posi]
            posi += 1
    else:
        number += roma[posi]
        posi += 1
print(number)