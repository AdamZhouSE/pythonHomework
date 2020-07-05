def ifprime(num):
    if num==1:
        return False
    for t in range(2,num):
        if num%t==0:
            return False
    return True

n=int(input())
res=[]
for _ in range(n):
    res.append(input().split(" "))
result=[]
for h in res:
    temp=int(h[0])+int(h[1])
    count=1
    while not ifprime(temp+count) :
        count+=1
    result.append(count)
for t in result:
    print(t)