def spiralOrder(matrix):
    if not matrix:
        return []

    cds = [1, 0, -1, 0] # 列坐标步进方向
    rds = [0, 1, 0, -1] # 行坐标步进方向

    # 行列当前元素数量（步进数）
    rs, cs = len(matrix), len(matrix[0])
    turns = 0 # 拐弯次数
    r, c = 0, -1 # 当前元素坐标
    elem_num = rs * cs
    result = [0] * elem_num # 结果
    index = 0 # 当前结果下标

    while index < elem_num:
        di = turns % 4 # 步进方向下标

        # 每次拐弯，交替使用行和列的步进
        steps = cs if turns % 2 == 0 else rs
        for i in range(steps):
            r += rds[di]
            c += cds[di]
            result[index] = matrix[r][c]
            index += 1

        # 每两次拐弯，行列的步进数递减
        if turns % 2 == 0:
            cs -= 1
            rs -= 1

        turns += 1

    return result


t = int(input())
for ti in range(t):
    s = input()
    m = int(s.split(' ')[0])
    n = int(s.split(' ')[1])
    line = input().split(' ')
    #print(line)
    data =[]
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(line[i*n+j])
        data.append(temp)
    #data = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    
    dat = spiralOrder(data)
    for i in dat:
        print(i,end=' ')
    print()
    
    
    
    
    
    
    
    
    