n=int(input())
arr=input().split()
for i in range(0,n):
    arr[i]=int(arr[i])
res=0
p=True
for i in range(1,min(arr)+1):
    for j in range(0,n):
        if arr[j]%i!=0:
            p=False
            break
    if p:
        res+=1
    p=True
print(res)
