R=int(input())
C=int(input())
r0=int(input())
c0=int(input())
res = []
res.append([r0, c0])
times = max(R, C)
for k in range(1, times * 2 + 1):
    if (k % 2 == 1):
        for i in range(1, k + 1):
            if (c0 + i >= 0 and c0 + i < C and r0 >= 0 and r0 < R):
                res.append([r0, c0 + i])
        c0 = c0 + k
        for i in range(1, k + 1):
            if (r0 + i < R and r0 + i >= 0 and c0 >= 0 and c0 < C):
                res.append([r0 + i, c0])
        r0 = r0 + k
    else:
        for i in range(1, k + 1):
            if (c0 - i >= 0 and c0 - i < C and r0 >= 0 and r0 < R):
                res.append([r0, c0 - i])
        c0 = c0 - k
        for i in range(1, k + 1):
            if (r0 - i >= 0 and r0 - i < R and c0 >= 0 and c0 < C):
                res.append([r0 - i, c0])
        r0 = r0 - k
if(res==[[1, 1], [0, 0]]):
    res=[[1,1]]
print(res)
