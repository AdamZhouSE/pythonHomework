def maxCount(m, n, ops):
    import sys
    if len(ops) == 0:
        return m*n;

    min_row = sys.maxsize
    min_col = sys.maxsize

    for pair in ops:
        min_row = min(min_row, pair[0])
        min_col = min(min_col, pair[1])
    return min_row * min_col

m=int(input())
n=int(input())
lops=int(input())
ops=[]
for i in range(lops):
    s=input()
    l=s.split(',')
    l= list(map(int, l))
    ops.append([l[0], l[1]])
print(maxCount(m,n ,ops))