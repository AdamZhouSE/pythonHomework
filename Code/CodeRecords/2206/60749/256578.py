def Fn(n):
    if n==1:
        return 1
    temp=1

    for i in range(int((n-1)*(n)/2)+1,int((n-1)*(n)/2+n+1)):
        temp=temp*i

    return temp
def sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=Fn(i)
    return sum

n=int(input())
res=[]
for _ in range(n):
    res.append(int(input()))
for k in res:

    print(sum(k), end="\n")