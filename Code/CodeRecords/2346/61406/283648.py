T = int(input())
for a in range(0,T):
    mn = input().split(' ')
    m = int(mn[0])
    n = int(mn[1])
    element = input().split(' ')
    matrix = [[],[],[],[]]
    for i in range(0,m):
        for j in range(0,n):
            matrix[i].append(0)
    for i in range(0,len(element)):
        matrix[i//4][i%4]=element[i]
    result = ""
    x=y=r=0
    count = 0
    while count<m*n:
        for y in range(y,n-r):
            result = result+" "+matrix[x][y]
            count+=1
        if count==m*n:
            break
        for x in range(x+1,m-r):
            result = result+" "+matrix[x][y]
            count += 1
        for y in range(y-1,r-1,-1):
            result = result+" "+matrix[x][y]
            count += 1
        if count==m*n:
            break
        for x in range(x-1,r,-1):
            result = result+" "+matrix[x][y]
            count += 1
        y+=1
        r+=1
    print(result.lstrip(" ")+" ")
