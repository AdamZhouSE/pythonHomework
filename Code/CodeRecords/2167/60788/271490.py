def min_path(matrix,start,end):
    if start==end:
        return 100
    else:
        
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
s=0
for i in range(node_num-1):
    for j in range(i+1,node_num):
        if colors[i]-colors[j]>=L or colors[i]-colors[j]<=-L:
            s+=min_path(matrix,i,j)
print(s)





