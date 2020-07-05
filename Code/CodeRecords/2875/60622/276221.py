n=int(input())
arr=list(map(int,input().split()))
ans=[0]*n
for i in range(n):
    ans[arr[i]-1]=i+1
print(" ".join(str(i) for i in ans))
