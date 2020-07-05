# 实际上是在求完全平方数的个数
n=int(input())

ans=0
i=1
while i*i<n:
    ans+=1
    i+=1

print(ans)

