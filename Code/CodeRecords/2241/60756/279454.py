N=int(input())
arr=[i for i in range(1,N+1)]
ans=1
for L in range(2,N//2+N%2+1):
    for i in range(N//2):
        if sum(arr[i:i+L])==N:
            ans+=1
print(ans)