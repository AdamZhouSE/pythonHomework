k=int(input())
n=int(input())
res=0
num=[0 for i in range(k+1)]
if k==1 and n==1:
    res=1
while(num[k]<n):
    for i in range(k,0,-1):
        num[i]=num[i]+num[i-1]+1
    res=res+1
print(res)