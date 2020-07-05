num=input().replace("[","").replace("]","").split(",")
arr=[]
for i in num:
    arr.append(int(i))
arr.sort()
for i in arr:
    if i<0:
        arr.remove(i)
for i in range(len(arr)):
    if arr[i]!=i+1:
        min=i+1
        break
if i==len(arr)-1:
    min=arr[-1]+1
print(min)