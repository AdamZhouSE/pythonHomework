num = int(input())
for i in range(num):
    n=int(input())
    numListStr = input().split()
    numList = []
    for element in numListStr:
        numList.append(int(element))
    numList.sort(reverse=True)
    add=numList[0]
    for index in range(1,len(numList)):
        if add>=numList[index]:
            add=add-numList[index]
        else:
            add=numList[index]-add
    print(add)