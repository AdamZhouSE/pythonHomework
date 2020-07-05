def isValid(n):
    num=0
    for i in range(1,n+1,1):
        if n%i==0:
            num=num+1
        else:
            pass
    if num==2:
        return True
    else:
        return False
def isUgly(n,l):
    for i in range(2,n+1,1):
        if n%i==0:
            if isValid(i):
                if i in l:
                    pass
                else:
                    return False
            else:
                pass
    return True
num=int(input())
l=input().split(",")
for i in range(len(l)):
    l[i]=int(l[i])
res=1
while num>0:
    if isUgly(res,l):
        res=res+1
        num=num-1
    else:
        res=res+1
print(res-1)
        
    