def numOfZero(n):
    temp=1
    for i in range(1,n+1):
        temp*=i
    s=str(temp)
    re=0
    for i in range(len(s)-1,0,-1):
        if s[i]=="0":
            re+=1
        else:
            break
    return re

k=int(input())
re=0
i=0
while True:
    if numOfZero(i)==k:
        re+=1
    if numOfZero(i)>k:
        break
    i+=1
print(re)