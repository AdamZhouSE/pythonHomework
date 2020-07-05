numList = [int(x) for x in input().split(",")]
length = len(numList)
globallll = 0
parttttt = 0
for i in range(0,length-1):
    for j in range(i+1,length):
        if numList[i]>numList[j]:
            if(j == i+1):
                parttttt+=1
                globallll+=1
            else:
                globallll+=1
if(parttttt==globallll):
    print(True)
else:
    print(False)