n=int(input())
num=input().split(" ")
arr=[]
count=1
for i in range(n-1):
    if num[i]==num[i+1]:
        count+=1
        if i==n-2:
            arr.append(count)
    else:
        arr.append(count)
        count=1
ans=0
for j in range(len(arr)-1):
    if min(arr[j],arr[j+1])>ans:
        ans=min(arr[j],arr[j+1])
print(2*ans)

