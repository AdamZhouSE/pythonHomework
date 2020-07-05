n=int(input())
numlist=list(map(int,input().split( )))
a=numlist.copy()
b=numlist.copy()
if(numlist[0]==3):
    a[0]=1
    b[0]=2
def minday(numlist):
    for i in range(len(numlist)):
        if(numlist[i]==3):
            if(numlist[i-1]==1):
                numlist[i]=2
            elif numlist[i-1]==2:
                numlist[i]=1
        elif numlist[i]!=0 and i!=0:
            if(numlist[i]==numlist[i-1]):
                numlist[i]=0
    re=0
    for i in numlist:
        if i==0:
            re+=1
    return re
print(min(minday(a),minday(b)))
