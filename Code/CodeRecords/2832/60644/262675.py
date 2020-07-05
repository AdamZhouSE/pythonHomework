num=int(input())
arr=input().split()
for i in range(0,len(arr)):
    arr[i]=int(arr[i])-1
res=0
end=0
for i in range(0,len(arr)):
    if arr[i]==end:
        res=res+1


    if arr[i]>end:
        end=arr[i]
p=True
for i in range(0,len(arr)-1):
    if arr[i]==num-1:
        p=False
        break
if p:
    res=res+1
print(res)