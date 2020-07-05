N = int(input())
listAll = []
for a in range(0,N):
    source = input()
    temp = []
    while len(temp) < 26:
        temp.append(0)
    for x in source:
        temp[ord(x)-65] = temp[ord(x)-65]+1
    listAll.append(temp)
y = 0
while y<len(listAll):
    if listAll.count(listAll[y])!=1:
        listAll.remove(listAll[y])
        y = y-1
    y = y+1
print(len(listAll),end='')


