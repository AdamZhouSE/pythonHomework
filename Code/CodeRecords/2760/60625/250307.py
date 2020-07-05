num = int(input())
for i in range(num):
    numListStr=input().split()
    numList=[]
    for element in numListStr:
        numList.append(int(element))

    print(numList[1]*(numList[0]//2+numList[0]%2))