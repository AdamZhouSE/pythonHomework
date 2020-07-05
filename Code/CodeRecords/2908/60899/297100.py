num = int(input())
list0 = []
for i in range(num):
    temp = input()
    listOftemp = []
    for j in range(len(temp)):
        listOftemp.append(temp[j])
    listOftemp.sort()
    str0 = "".join(listOftemp)
    list0.append(str0)
res = True
while res:
    res = False
    for x in list0:
        if list0.count(x)>1:
            list0.remove(x)
            res = True
            break
print(len(list0),end = "")