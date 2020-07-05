arr = list(map(int, input().split(" ")))
result = {}
for m in arr:
    if (m in result):
        result[m] += 1
    else:
        result[m] = 1
if (len(result) >= 4):
    print("Alien")
elif (len(result) == 3):
    situation = False
    for m in result.keys():
        if (result[m] == 4):
            situation = True
            print("Bear")
            break
    if (not situation):
        print("Alien")
elif (len(result) == 2):
    situation = False
    for m in result.keys():
        if (result[m] == 4 or result[m] == 2):
            situation = True
            print("Elephant")
            break
    if (not situation):
        if(5 in result.values()):
            print("Bear")
        else:
            print("Alien")
else:
    print("Elephant")