arr=input()
arr=arr[1:len(arr)-1].split(",")
arr.sort()
flag=True
for i in range(1,len(arr)):
    if arr.count(str(i))==0:
        print(i)
        flag=False
        break
if flag:print(len(arr))