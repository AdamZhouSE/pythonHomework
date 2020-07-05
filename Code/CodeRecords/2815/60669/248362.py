n=int(input())
arr=list(map(int,input().split()))
negative=[]
positive=[]
zero=[]
result=0
for x in arr:
    if x<0:
        negative.append(x)
    elif x>0:
        positive.append(x)
    else:
        zero.append(x)
if (len(negative)%2==0) or (len(negative)%2==1 and len(zero)!=0):
    for item in negative:
        result+=(-1-item)
    for item in positive:
        result+=(item-1)
    for item in zero:
        result+=1
else:
    negative.sort()
    for i in range(0,len(negative)):
        if i==len(negative)-1:
            result+=(1-negative[i])
        else:
            result+=(-1-negative[i])
    for item in positive:
        result+=(item-1)
        
print(result)