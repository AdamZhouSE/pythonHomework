num = int(input())
for i in range(num):
    number=int(input())
    TList=input().split()
    CanList=list(set(TList))
    TNList=[]
    count=0
    for candidate in CanList:
        TNList.append(0)
        for index in range(len(TList)):
            if candidate==TList[index]:
                TNList[count]=TNList[count]+1
        count=count+1

    for j in range(len(TNList)):
        for l in range(len(TNList) - 1):
            if TNList[l] < TNList[l + 1]:
                temp = TNList[l]
                TNList[l] = TNList[l + 1]
                TNList[l + 1] = temp

                temp = CanList[l]
                CanList[l] = CanList[l + 1]
                CanList[l + 1] = temp

    MaxCan=[]
    MaxCan.append(CanList[0])
    for nI in range(len(TNList)-1):
        if TNList[nI]!=TNList[nI+1]:
            break
        elif TNList[nI]==TNList[nI+1]:
            MaxCan.append(CanList[nI+1])
    MaxCan.sort()
    print(MaxCan[0]+' '+str(TNList[0]))