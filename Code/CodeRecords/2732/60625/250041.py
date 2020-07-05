num = int(input())
for i in range(num):
    List=input().split()
    numList=[]
    for element in List:
        numList.append(int(element))

    print(numList[0]**numList[1]%numList[2])