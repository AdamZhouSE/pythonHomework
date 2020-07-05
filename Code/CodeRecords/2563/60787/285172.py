def cal(n,k):
    re=[]
    if k==1:
        re.append(n)
    else:
        while n>0:
            re.insert(0,n%k)
            n=int(n/k)
    return re

n=int(input())
k=1
while True:
    temp=cal(n,k)
    for i in range(0,len(temp)):
        if temp[i]!=1:
            break
    else:
        break
    k+=1
print(k)