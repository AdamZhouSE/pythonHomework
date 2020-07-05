num=int(input())
arr=input().split()
for i in range(0,num):
    arr[i]=int(arr[i])
n1=arr.count(5)
n2=arr.count(0)
res=-1
if n2>0:
    res=0
    if n1>=9:
        res='5'*int(n1/9)*9+'0'*n2
print(res)
