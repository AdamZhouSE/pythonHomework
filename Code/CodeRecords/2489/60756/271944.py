arr=list(map(int,input()[1:-1].split(",")))
lower=int(input())
upper=int(input())
ans=0
for L in range(len(arr)):
    for i in range(len(arr)-L):
        if lower<=sum(arr[i:i+L+1])<=upper:
            ans+=1
print(ans)