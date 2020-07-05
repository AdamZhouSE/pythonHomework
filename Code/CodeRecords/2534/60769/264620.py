arr = eval(input())
ptr = [0] * len(arr)
res = []
while len(ptr) != 0:
    temp = []
    for i in range(len(ptr)):
        temp.append(arr[i][ptr[i]])
    res.append(min(temp))
    index = temp.index(res[-1])
    ptr[index] += 1
    if ptr[index] == len(arr[index]):
        ptr.pop(index)
        arr.pop(index)
print(res)
