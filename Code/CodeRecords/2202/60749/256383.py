def howmany(num):
    if num==1:
        return 1
    elif num==2:
        return 2
    else:
        return howmany(num-1)+howmany(num-2)
n=int(input())
res=[]
for _ in range(n):
    res.append(int(input()))
for t in res:
    print(howmany(t))