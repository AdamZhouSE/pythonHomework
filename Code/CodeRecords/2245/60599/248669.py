def toB(k):
    tmp=""
    while k!=0:
        if(k%2==0):
            tmp="0"+tmp
        else:
            tmp="1"+tmp
        k//=2
    return tmp

n=int(input())
b=toB(n)
maxL=0
last=-1
for i in range(len(b)):
    if(b[i]=='1'):
        if(last==-1):
            last=i
            continue
        maxL=max(maxL,i-last)
        last=i
print(maxL)


