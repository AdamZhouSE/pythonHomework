def maxsublist(numlist,n):
    numlist.sort()
    maxlen=1
    templen=1
    for i in range(1,n):
        if(numlist[i]==numlist[i-1]+1):
            templen+=1
        else:
            maxlen=max(maxlen,templen)
            templen=1
    return maxlen

t=int(input())
for i in range(t):
    n=int(input())
    numlist=list(map(int,input().split(" ")))
    print(maxsublist(numlist,n))