def find(arr,x):
    ind=arr.index(x)
    if arr[ind-1]-arr[ind]>arr[ind+1]-arr[ind]:
        return ind+1
    else:
        return ind-1
    
arr=eval(input())
k=int(input())
x=int(input())
li=[]
if arr.count(x)>0:
    for i in range(arr.count(x)):
        li.append(x)
    if len(li)>k:
        n=len(li)-k
        for i in range(n):
            del li[0]
        k=0
    else:
        k=k-len(li)
    enough=arr.count(x)
    for i in range(enough-1):
        del arr[arr.index(x)]
else:
    arr.append(x)
    arr=sorted(arr)
for i in range(k):
    ind=find(arr,x)
    li.append(arr[ind])
    del arr[ind]
print(sorted(li))
    
    
