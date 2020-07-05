numOftests = int(input())
for i in range(numOftests):
    list0 = list(map(int,input().split()))
    m = list0[0]
    n = list0[1]
    list1 = list(map(int,input().split()))
    matrix = [[0 for x in range(n)] for y in range(m)]
    for j in range(m):
        for k in range(n):
            matrix[j][k] = list1[j*n+k]
    beginX = 0
    endX = n - 1
    beginY = 0
    endY = m - 1
    result = []
    while True:
        #从左上到右上
        for j in range(beginX,endX+1): 
            result.append(matrix[beginY][j])
        beginY+=1
        if beginY > endY:break
        #从右上到右下
        for j in  range(beginY,endY+1):
            result.append(matrix[j][endX])
        endX -=1
        if  endX < beginX :
            break
        # 从右下到左下
        for j in range(endX,beginX-1,-1):
            result.append (matrix[endY][j])
        endY -=1
        if  endY < beginY :
            break
        # 从左下到左上
        for j in range(endY,beginY-1,-1) :
            result.append (matrix[j][beginX])
        beginX +=1
        if  beginX > endX :
            break
    list2 = list(map(str,result))
    str1 = ' '.join(list2)
    print(str1+" ")




