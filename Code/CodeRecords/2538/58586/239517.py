arr=eval(input())
arr.sort()
index=-1
for i in range(len(arr)):
    if arr[i]>0:
        index=i
        break
if index==-1:
    print(1)
if arr[index]>1:
    print(1)
else:
    idx=-1
    for i in range(index,len(arr)-1):
        if arr[i+1]-arr[i]!=1:
            print(arr[i]+1)
            idx=i
            break
    if idx==-1:
        print(arr[-1]+1)
        
