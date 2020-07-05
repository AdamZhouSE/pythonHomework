num = int(input())
for i in range(num):
    numList=list(input())

    while len(numList)>1:
        add = 0
        for i in numList:
            add=add+int(i)
        numstr=str(add)
        numList=list(numstr)
    print(numList[0])