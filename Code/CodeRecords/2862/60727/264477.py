def so(x,num):
    x=sorted(x)
    temp=0
    numOfj=0
    numOfo=0
    for i in x:
        if i%2==0:
            numOfo+=1
        else:
            numOfj+=1
    if numOfo==numOfj or abs(numOfo-numOfj)==1:
        return 0
    res=0
    if numOfo>numOfj:
        temp=0
        diff=numOfo-numOfj-1
        for i in x:
            if i%2==0:
                res+=i
                temp+=1
            if temp==diff:
                break
    else:
        temp=0
        diff=-numOfo+numOfj-1
        for i in x:
            if i%2==1:
                res+=i
                temp+=1
            if temp==diff:
                break
    return res
        
num = int(input())
x=input().split(' ')
x=list(map(int,x))
print(so(x,num))