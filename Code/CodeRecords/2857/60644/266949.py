n=int(input())
arr=input().split()
for i in range(0,n):
    arr[i]=int(arr[i])
for i in range(0,n):
    for j in range(0,n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
res=0
p=True
for i in range(1,arr[0]+1):
    for j in range(0,n):
        if arr[j]%i!=0:
            p=False
            break
    if p:
        res+=1
    p=True
print(res)
