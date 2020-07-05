def find_shorted_dis(matrix,dist,row_size,col_size):
    min_dist=row_size+col_size
    for i in range(row_size):
        for j in range(col_size):
            cur_len=dfs(i,j,matrix,dist,row_size,col_size)
            dist[i][j]=cur_len
    return dist


def dfs(i,j,matrix,dist,row_size,col_size):
    #该函数直接对dist数组的值进行修改  不用返回
    if matrix[i][j] == '0':
        return 0
    else:
        for x_offset, y_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x = i + x_offset
            y = j + y_offset
            if x < 0 or x >= row_size or y < 0 or y >= col_size:
                continue
            else:
                return 1 + dfs(x,y,matrix,dist,row_size,col_size)


if __name__=="__main__":
    matrix=[]
    while True:
        try:
            matrix.append(input())
        except:
            break
    matrix=[x.split() for x in matrix]
    # print(matrix)
    row_size=len(matrix)
    col_size=len(matrix[0])
    dist=[([-1]*col_size) for i in range(row_size)]#注意不能是浅拷贝 否则不能修改二维数组的值
    # print(dist)
    ans=find_shorted_dis(matrix,dist,row_size,col_size)
    # print(ans)
    for i in ans:
        i=[str(x) for x in i]
        s=" ".join(i)
        print(s)
