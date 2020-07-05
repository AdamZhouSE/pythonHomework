n,k=map(int,input().split(' '))
arr=list(map(int,input().split(' ')))
temp=-1
sum=0
for i in range(n):
    if(temp==-1):
        temp=arr[i]
        arr[i]=0
    else:
        arr[i]-=temp
        temp+=arr[i]
    sum+=arr[i]
list.sort(arr)
for i in range(n-1,-1,-1):
    if(k==1):
        break
    else:
        k-=1
        sum-=arr[i]
print(sum)