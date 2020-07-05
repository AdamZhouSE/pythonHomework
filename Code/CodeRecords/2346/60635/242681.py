count = int(input())


def add_to_list (matrix, ans):
    if len(matrix) == 0:
        return
    elif len(matrix) == 1:
        for m in matrix[0]:
            ans.append(m)
        return
    elif len(matrix) <= 2:
        for m in matrix[0]:
            ans.append(m)
        for i in range(len(matrix[0])-1,-1,-1):
            ans.append(matrix[1][i])
        return
    row, col = 0,len(matrix[0])-1
    for i in range(col+1):
        ans.append(matrix[0][i])
    while row < len(matrix)-1:
        row += 1
        ans.append(matrix[row][col])
    for i in range(col-1,-1,-1):
        ans.append(matrix[row][i])
    for i in range(row-1,0,-1):
        ans.append(matrix[i][0])
    del matrix[row]
    del matrix[0]
    add_to_list([x[1:col] for x in matrix], ans)
    return


for i in range(count):
    info = input().split()
    m = int(info[0])
    n = int(info[1])
    matrix = [[] for i in range(m)]
    src = input().split()
    for j in range(len(src)):
        matrix[j // n].append(src[j])
    ans=[]
    add_to_list(matrix,ans)
    print(' '.join(ans),end = ' \n')