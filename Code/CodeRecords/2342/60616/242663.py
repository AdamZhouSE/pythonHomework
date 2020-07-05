def rotate(items,startIndex,endIndex):
    while(startIndex<=endIndex):
        temp=items[startIndex]
        items[startIndex]=items[endIndex]
        items[endIndex]=temp
        startIndex=startIndex+1
        endIndex=endIndex-1
    return items

testNum=int(input())
for i in range (testNum):
    rawInputs=input().split(' ')
    n=int(rawInputs[0])
    k=int(rawInputs[1])
    rawItems=input().split(' ')
    items=[]
    for rawItem in rawItems:
        items.append(int(rawItem))
    partNum=0
    if(n%k==0):
        partNum=int(n/k)
        for x in range (0,partNum+k,k):
            rotate(items,x,x+k-1)
        print(" ".join(str(i) for i in items),'')

    if(n%k>0):
        partNum=int(n/k)
        for y in range(0,partNum+k-1,k):
            rotate(items, y, y + k-1)
        rotate(items,partNum*k,n-1)
        print(" ".join(str(i) for i in items),'')