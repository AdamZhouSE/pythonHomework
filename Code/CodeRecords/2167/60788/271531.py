import copy
def min_path(matrix1, start, end):
    if start == end:
        return -1
    else:
        min_value = 1000
        adjacent = find_adjacent(start, matrix1)
        for i in adjacent:
            new_matrix = copy.deepcopy(matrix1)
            new_matrix[start][i] = 0
            new_matrix[i][start] = 0
            s1 = max(matrix1[start][i], min_path(new_matrix, i, end))
            min_value = min(min_value, s1)
        return min_value

        
def find_adjacent(node,matrix):
    s=[]
    for i in range(len(matrix)):
        if matrix[node][i]!=0:
            s.append(i)
    return s

line1=input().strip()
line2=input().strip()
node_num=int(line1.split()[0])
edge_num=int(line1.split()[1])
L=int(line1.split()[2])
colors=[int(x) for x in line2.split()]
matrix=[[0]*node_num for i in range(node_num)]
for i in range(edge_num):
    line=input().strip()
    matrix[int(line.split()[0])-1][int(line.split()[1])-1]=int(line.split()[2])
    matrix[int(line.split()[1])-1][int(line.split()[0])-1]=int(line.split()[2])
s=0
for i in range(node_num-1):
    for j in range(i+1,node_num):
        if colors[i]-colors[j]>=L or colors[i]-colors[j]<=-L:
            s+=min_path(matrix,i,j)
print(s)





