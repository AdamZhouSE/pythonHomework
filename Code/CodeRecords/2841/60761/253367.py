def printVal(numlist):
    while(len(numlist)>1):
        orlist=[]
        xorlist=[]
        for i in range(0,len(numlist),2):
            orlist.append(numlist[i]|numlist[i+1])
        if(len(orlist)==1):
            return orlist[0]
        for i in range(0,len(orlist),2):
            xorlist.append(orlist[i]^orlist[i+1])
        numlist=xorlist
    return numlist[0]
n,m=map(int,input().split(" "))
numlist=list(map(int,input().split(" ")))
for i in range(m):
    p,b=map(int,input().split(" "))
    numlist[p-1]=b
    print(printVal(numlist))