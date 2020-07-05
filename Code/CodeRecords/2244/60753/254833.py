
def isSushu(a):
    if a<=1:
        return 0
    else:
        valid=1
        for i in range(2,a):
            if a%i==0:
                valid=0
                break
        return valid
def isHuiwen(a):
    stra=str(a)
    length=len(stra)
    valid=1 
    for i in range(int(length/2)):
        if stra[i]!=stra[length-1-i]:
            valid=0
            break
    return valid
n=input()
judge1=isSushu(n)
judge2=isHuiwen(n)
while judge1!=1 or judge2!=1:
    n+=1
    judge1=isSushu(n)
    judge2=isHuiwen(n)
print(n)