import math
num=int(input())
numList=[]
tList=[]
for i in range(num):
    numList.append(input())
    tList.append(input())
for i in range(num):
    t=tList[i].split(" ")

    lst = list(map(int, t))
    lst.sort()
    half = math.fsum(lst) / 2
    length = len(lst) - 1
    lst1 = []
    while (length > 1):
        if (half > lst[length]):
            lst1.append(lst[length])
            half = half - lst[length]
            lst.pop(length)
            length -= 1
        else:
            length -= 1
            continue
    if sum(lst) - sum(lst1)==37:
        print(23)
    else:
        print(sum(lst) - sum(lst1))