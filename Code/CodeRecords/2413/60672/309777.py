def ans(n,start):
    res=[]
    for i in range(1<<n):
        res.append(i^(i>>1))
    while res[0]!=start:
        res.append(res.pop(0))
    return res

n=input()
start=input()
answer=ans(n,start)
print(answer)