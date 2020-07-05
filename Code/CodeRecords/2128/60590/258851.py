A = list(map(int, input().split(",")))

def func(lists):
    res = 0
    for i in range(len(lists)):
        res += (i * int(lists[i]))
    return res

def rotate(lists):
    arr = []
    arr.append(lists[lists.__len__()-1])
    for i in range(len(lists)-1):
        arr.append(lists[i])
    return arr

arr = []
for i in range(A.__len__()):
    temp = func(A)
    arr.append(temp)
    A = rotate(A)

ans = max(arr)
print(ans)