times = int(input())
names = []
judeg = []
for i in range(times):
    name = input()
    names.append(name)
    judeg.append(True)
n = int(input())
for j in range(n):
    temp = input()
    if temp in names:
        index = names.index(temp)
        if judeg[index]:
            print("OK")
            judeg[index] = False
        else:
            print("REPEAT")
    else:
        print("WRONG")
