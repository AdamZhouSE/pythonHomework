def maxS(matrix, k) -> int:
    import bisect
    row = len(matrix)
    col = len(matrix[0])
    res = float("-inf")
    for left in range(col):
        _sum = [0] * row
        for right in range(left, col):
            for j in range(row):
                _sum[j] += matrix[j][right]
            arr = [0]
            cur = 0
            for tmp in _sum:
                cur += tmp
                loc = bisect.bisect_left(arr, cur - k)
                if loc < len(arr):res = max(cur - arr[loc], res)
                bisect.insort(arr, cur)
    return res

row=int(input())
mat=[]
for i in range(row):
    aaa=input()
    l1=aaa.split(",")
    l1= list(map(int, l1))
    mat.append(l1)
k=int(input())
print(maxS(mat,k))