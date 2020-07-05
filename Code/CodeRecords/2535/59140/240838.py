def block(arr):
    if len(arr)==1:return 1
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[len(arr)-1-i]:
                return 1
        return 1+block(arr[0:len(arr)-1-i])


str = input()
arr = []
for x in list(str):
    try:
        arr.append(int(x))
    except:
        pass
print(block(arr))