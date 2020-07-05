def isI(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def isH(num):
    str1=str(num)
    s=0
    e=len(str1)-1
    while(s<e):
        if str1[s]!=str1[e]:
            return False
        else:
            s+=1
            e-=1
    return True
n=int(input())
while True:
    if not isH(n):
        n+=1
    else:
        if not isI(n):
            n+=1
        else:
            break
print(n)
