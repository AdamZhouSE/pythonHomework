num = int(input())
for i in range(num):
    numListStr=input().split()
    numList=[]
    for element in numListStr:
        numList.append(int(element))
    count=0
    for number in range(numList[0],numList[1]+1):
        if number%numList[2]==0:
            count=count+1
        elif number%numList[3]==0:
            count=count+1
    print(count)