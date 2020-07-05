n=int(input())
a=list(map(int,input().split()))
odd=[]
evan=[]
sum=0
for i in range(n):
    if a[i]%2==0:
        evan.append(a[i])
    else:
        odd.append(a[i])
    sum+=a[i]
res=len(evan) if sum%2==0 else len(odd)
print(res
)