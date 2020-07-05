n=int(input())
numList=list(map(int,input().split()))
method=0
partialSum=0
searchList=[]
for i in numList:
    partialSum+=i
    searchList.append(partialSum)
divideNum=searchList.pop()
if divideNum%3==0:
    while divideNum//3 in searchList:
        beginLoc=searchList.index(divideNum//3)
        searchList=searchList[beginLoc+1:]
        method+=(searchList.count(divideNum*2//3))
if divideNum==0:
    method+=2
print(method)