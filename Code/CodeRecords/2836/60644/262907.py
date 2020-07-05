num=int(input())
arr=input().split()
for i in range(0,num):
    arr[i]=int(arr[i])
res=-1
sum=0
for i in range(0,num):
    arr[0],arr[-1]=arr[-1],arr[0]
    p=True
    for j in range(0,num-1):
        if arr[j]>arr[j+1]:
            p=False
            break
    sum=sum+1
    if p:
        res=sum
        break
print(res)
