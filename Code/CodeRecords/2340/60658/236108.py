t = int(input())
for i in range(t):
    n = int(input())
    li = [int(x) for x in input().split()]
    ans = 0
    for i in range(1,n-1):
        temp = min(max(li[:i]),max(li[i+1:]))-li[i]
        ans+= temp if temp>0 else 0 
    print(ans)