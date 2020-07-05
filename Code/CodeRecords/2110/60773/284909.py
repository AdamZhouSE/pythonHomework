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
def isUgly(n):
    for i in range(2,n,1):
        if n%i==0:
            if isValid(i):
                if i!=2 and i!=3 and i!=5:
                    return False
            else:
                pass
    return True
n=int(input())
print(isUgly(n))