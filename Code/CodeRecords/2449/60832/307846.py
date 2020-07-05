ar = list(map(int, input().split(',')))
n=int(input())

ans=-1
for i in len(ar):
    if n==ar[i]:
        ans=i+1
        break
print(ans)