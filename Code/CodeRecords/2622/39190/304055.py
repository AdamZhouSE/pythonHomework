def func11(arr):
    tmp=[]
    for i in range(len(arr)):
        try:
            tmp.index(arr[i])
            if arr.count(arr[i])>len(arr)/2:
                return arr[i]
                tmp.append(arr[i])
        except ValueError:
            tmp.append(arr[i])
ip=input().split(",")
op=func11(ip)
print(op)