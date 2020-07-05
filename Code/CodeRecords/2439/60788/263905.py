import copy
def f(start, end, matrix):
    if matrix[start][end] != 0:
        return matrix[start][end]
    next_nodes = find_adjacent(start, matrix)
    if len(next_nodes) == 0:
        return 0
    else:
        t = []
        for i in next_nodes:
            new_matrix=copy.deepcopy(matrix)
            new_matrix[start][i] = 0
            new_matrix[i][start] = 0
            if f(i, end, new_matrix)!=0:
                t.append(matrix[start][i]^f(i,end,new_matrix))
        s = 0
        for i in t:
            s = s ^ i
        return s
    
def find_adjacent(node,matrix):
    s=[]
    for i in range(len(matrix)):
        if matrix[node][i]!=0:
            s.append(i)
    return s


node_num=int(input())
s=[[0]*node_num for i in range(node_num)]
for i in range(node_num-1):
    line=input().strip()
    s[int(line.split()[0])-1][int(line.split()[1])-1]=int(line.split()[2])
    s[int(line.split()[1])-1][int(line.split()[0])-1]=int(line.split()[2])
question_num=int(input())
for i in range(question_num):
    line=input().strip()
    start=int(line.split()[0])
    end=int(line.split()[1])
    print(f(start-1,end-1,s))
    