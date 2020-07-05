arr1=list(map(int,input().split(",")))
arr2=list(map(int,input().split(",")))
max_val=-99999
for i in range(0,len(arr1)):
    for j in range(0,len(arr1)):
        temp=abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)
        max_val=max(max_val,temp)
print(max_val)