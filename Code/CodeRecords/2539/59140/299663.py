arr=input()
arr=arr[1:len(arr)-1].split(", ")
for i in range(len(arr)):
    arr[i]=int(arr[i])
newarr=arr.copy()
newarr.sort()
left=right=-1
for i in range(len(arr)):
    if newarr[i]!=arr[i]:
        left=i
        break
for i in range(len(arr)):
    if newarr[len(arr)-1-i]!=arr[len(arr)-1-i]:
        right=len(arr)-1-i
        break
if left==right==-1:print(0)
else:print(right-left+1)