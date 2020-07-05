import math
x=int(input())
y=int(input())
bound=int(input())
a=int(math.log(bound, x)) + 1 if x > 1 else 1
b=int(math.log(bound, y)) + 1 if y > 1 else 1
res=[]
k=0
for i in range(a):
    for j in range(b):
        k=x**i+y**j
        if k>bound:
            break
        res.append(k)
res.sort()
ans=[]
for i in res:
    if i not in ans:
        ans.append(i)
ans.sort()
print(ans)