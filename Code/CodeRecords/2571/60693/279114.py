import bisect
def findMaxSumUnderK(matrix:[[int]],k:int):
    row,col=len(matrix),len(matrix[0])
    res=float("-inf")
    for l in range(col):
        sum=[0]*row
        for r in range(l,col):
            for j in range(row):
                sum[j]+=matrix[j][r]
            arr=[0]
            cur=0
            for s in sum:
                cur+=s
                idx=bisect.bisect_left(arr,cur-k)
                if idx<len(arr):
                    res=max(cur-arr[idx],res)
                bisect.insort(arr,cur)
    return res


matrix=[]
n=int(input())
for _ in range(n):
    row=list(map(int,input().split(',')))
    matrix.append(row)
k=int(input())
print(findMaxSumUnderK(matrix,k))