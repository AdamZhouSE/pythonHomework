n=int(input())
k =list(map(int, input().split()))
cnt=1
ans=1
for i in range(n-1):
    if k[i]<k[i+1]:
        cnt=cnt+1
    else:
        cnt=1
    ans = max(cnt,ans)
print(ans)