A = [int(x) for x in input().split(',')]
A.sort()
A.reverse()
curIdx = 0
res = 0
while curIdx + 2 < len(A):
    if A[curIdx] < A[curIdx + 1] + A[curIdx + 2]:
        res = A[curIdx] + A[curIdx + 1] + A[curIdx + 2]
        break
    curIdx += 1
print(res)