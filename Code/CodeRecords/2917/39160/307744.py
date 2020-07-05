from collections import Counter
 
n = int(input())
x = Counter()
y = Counter()
xy  = Counter()
ans = 0
for _ in range(n):
    a,b = map(int,input().split())
    ans+= x[a] + y[b] - xy[(a,b)]
    x[a]+=1
    y[b]+=1
    xy[(a,b)]+=1
print(ans)