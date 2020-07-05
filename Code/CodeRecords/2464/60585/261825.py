s=eval(input())
arr=list(map(int,input().strip().split(',')))
n=len(arr)
minL=n+1
l=0
temp=0
for i in range(n):
    temp+=arr[i]
    while temp>=s:
        minL=min(i-l+1,minL)
        temp-=arr[l]
        l+=1
print(minL)