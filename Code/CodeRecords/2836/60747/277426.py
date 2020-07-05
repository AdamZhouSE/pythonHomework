n=int(input())
arr=input().split(" ")
arr2=[]
for i in range(len(arr)):
    arr[i]=int(arr[i])
    arr2.append(arr[i])
count=0
a=0
while(count!=len(arr)):
    arr2.sort()
    for j in range(len(arr)):
        if arr2[j]==arr[j]:
            continue
        else:
            a=-1
            break
    if a==-1:
        last=arr[len(arr)-1]
        k=len(arr)-1
        while k>0:
            arr[k]=arr[k-1]
            k=k-1
        arr[0]=last
        a=0
        count+=1
    else:
        break
    for h in range(len(arr)):
        arr2[h]=arr[h]
if count!=len(arr):
    print(count)
else:
    print(-1)
