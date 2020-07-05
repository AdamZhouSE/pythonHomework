def intToNbin(N):
    if N == 0:
        return [0]
    arr = []
    while N != 0:
        if N % 2 == 0:
            arr.append(0)
            N = N / (-2)
        else:
            arr.append(1)
            N = (N-1) / (-2)
    arr.reverse()
    return arr

def nbinToInt(arr):
    if arr == [0]:
        return 0
    N = 0
    base = (-2)**(len(arr)-1)
    for i in arr:
        N += base * i
        base /= -2
    return N

arr1 = list(map(int,input().split(',')))
arr2 = list(map(int,input().split(',')))
sum = int(nbinToInt(arr1)+nbinToInt(arr2))
res = intToNbin(sum)
print(res)