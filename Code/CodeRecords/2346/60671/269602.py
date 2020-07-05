def spiralOrder(matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans




time=int(input())
while(time>0):
    time-=1
    #初始化
    str0=input()
    list0=str0.split()
    row=int(list0[0])
    col=int(list0[1])
    #print(row,col)
    arr=[[0]*col for i in range(row)]
    str1=input()
    list1=str1.split()
    numList=[]
    for x in list1:
        numList.append(int(x))
    #print(numList)
    length=len(numList)
    for i in range(length):
        j=int(i/col)
        k=int(i%col)
        arr[j][k]=numList[i]
    #print(arr)
    
    ans=spiralOrder(arr)
    
    #print(arr)
    print(*ans,end=' \n')