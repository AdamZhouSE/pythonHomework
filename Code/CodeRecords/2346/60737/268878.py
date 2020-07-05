t = int(input())
while t:
    cmd = [int(n) for n in input().split( )]
    m, n = cmd[0], cmd[1]
    nums = [int(i) for i in input().split( )]
    mat = []
    ret = []
    for i in range(m):
        mat.append(nums[i*n:i*n+n])
    tag = [[0 for i in range(n)] for j in range(m)]
    i, j = 0, 0
    ret.append(mat[i][j])
    tag[i][j] = 1
    while (j+1<n and tag[i][j+1]==0) or (i+1<m and tag[i+1][j]==0) or (j-1>=0 and tag[i][j-1]==0) or (i-1 >=0 and tag[i-1][j]==0):
        while j+1 < n and tag[i][j+1] == 0:
            ret.append(mat[i][j+1])
            tag[i][j+1] = 1
            j += 1
        while i+1 < m and tag[i+1][j] == 0:
            ret.append(mat[i+1][j])
            tag[i+1][j] = 1
            i += 1
        while j-1>=0 and tag[i][j-1] == 0:
            ret.append(mat[i][j-1])
            tag[i][j-1] = 1
            j -= 1
        while i-1>=0 and tag[i-1][j] == 0:
            ret.append(mat[i-1][j])
            tag[i-1][j] = 1
            i -= 1
    for k in ret:
        print(k,end=" ")
    print()        
    
    t -= 1