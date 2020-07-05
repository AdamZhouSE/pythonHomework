ar = list(map(int, input().split(',')))
n=int(input())

ans=-1
for i in range(len(ar)):
    if n==ar[i]:
        ans=i
        break
print(ans)