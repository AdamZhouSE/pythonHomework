n=int(input())
m=int(input())
arr=[]
res=0
for i in range(0,n):
    arr=arr+[int(input())]
for i in range(0,n):
    for j in range(0,n-1):
        if arr[j]<arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
for i in range(0,n):
    m=m-arr[i]
    res+=1
    if m<=0:
        break
print(res)
