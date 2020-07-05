n,q=[int(i) for i in input().split()]
a=n*[n*[-1]]
for ques in range(q):
    ope=[int(i) for i in input().split()]
    if ope[0]==0:
        a[ope[1]][ope[2]]=ope[3]
        a[ope[2]][ope[1]]=ope[3]
    elif ope[0]==1:
        a[ope[1]][ope[2]]=-1
        a[ope[2]][ope[1]]=-1
    else:
        print(a[ope[1]][ope[2]])
def floyd(data_matrix):
    '''
    输入：原数据矩阵，即：一个二维数组
    输出：顶点间距离
    '''
    dist_matrix=[]
    path_matrix=[]
    vex_num=len(data_matrix)  
    for h in range(vex_num):
        one_list=['N']*vex_num
        path_matrix.append(one_list)
        dist_matrix.append(one_list)
    for i in range(vex_num):
        for j in range(vex_num):
            dist_matrix=data_matrix
            path_matrix[i][j]=j
    for k in range(vex_num):
        for i in range(vex_num):
            for j in range(vex_num):
                if dist_matrix[i][k]=='N' or dist_matrix[k][j]=='N':
                    temp='N'
                else:
                    temp=dist_matrix[i][k]+dist_matrix[k][j]
                if dist_matrix[i][j]>temp:
                    dist_matrix[i][j]=temp
                    path_matrix[i][j]=path_matrix[i][k]
    return dist_matrix, path_matrix