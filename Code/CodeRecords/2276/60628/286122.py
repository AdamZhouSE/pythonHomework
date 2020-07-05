def spiralMatrix(R,C,r0,c0):
    i,j = r0,c0
    cnt = 1
    step = 1
    direct = 0
    increment = [(0,1),(1,0),(0,-1),(-1,0)]
    res = [[r0,c0]]
    while cnt < R*C:
        for _ in range(step):
            i += increment[direct][0]
            j += increment[direct][1]
            if i >= 0 and i < R and j >= 0 and j < C:
                cnt += 1
                res.append([i,j])
        if(direct == 1 or direct == 3):
            step += 1
        direct = (direct + 1)%4
    return res

R = int(input())
C = int(input())
r0 = int(input())
c0 = int(input())
print(spiralMatrix(R,C,r0,c0))