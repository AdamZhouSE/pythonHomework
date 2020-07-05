n=int(input())
li=list(map(int,input().split()))
days=0
for i in range(1,n+1):
    mint=max(li)
    if mint<i:
        break
    for j in range(len(li)):
        if li[j]>=i and li[j]<mint :
            mint=li[j]
    li.remove(mint)
    days=days+1
print(days)
