n=int(input())
arr=[int(n) for n in input().split(' ')]
sum=0
re=[]
for i in range(0,len(arr)):
    if arr[i]==1:
        if i==0:
            continue
        else:
            sum=sum+1
            re.append(arr[i-1])
    if i==len(arr)-1:
        sum=sum+1
        re.append(arr[i])
print(sum)
for i in range(0,len(re)-1):
    print(re[i],end=" ")
print(re[len(re)-1])