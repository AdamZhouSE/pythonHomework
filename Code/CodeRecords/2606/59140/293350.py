arr=input()
arr=arr[1:len(arr)-1].split(",")
target=input()
if arr.count(target)==1:print(arr.index(target))
else:print(-1)