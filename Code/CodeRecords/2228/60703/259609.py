
def reachNumber (target):
    target = abs(target)
    k = 0
    while target>0:
        k+=1
        target -=k
    if(target%2==0):
        return k
    else:
        target = abs(target)
        if((target+k+1)%2==0):
            return k+1
        else:
            return k+2

n = int(input())
print(reachNumber(n))