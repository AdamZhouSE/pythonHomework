s = input()
t = input()
sList = list(s)
tList = list(t)

flag = False
index = 0
for i in range(sList.__len__()):
    #print(index)
    #print(flag)
    for j in range(index, tList.__len__()):
        if tList[j] == sList[i]:
            index += 1
            flag = True
            break
        else:
            index += 1
            flag = False

print(flag)