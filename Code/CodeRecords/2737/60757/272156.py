import math
arr=list(eval(input()))
m=math.floor(len(arr)/3)
li=[]
for i in range(len(arr)):
    if arr.count(arr[i])>m:
        li.append(arr[i])
li=list(tuple(set(li)))
print(li)