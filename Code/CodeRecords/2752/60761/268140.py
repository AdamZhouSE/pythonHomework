input()
a=input()
matrix=[]
heights=[]
trees=[]
while(a!="]"):
    if(a.endswith(",")):
        matrix.append(list(map(int,a[2:-2].split(","))))
    else:
        matrix.append(list(map(int,a[2:-1].split(","))))
    a=input()
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if(matrix[i][j]!=0):
            trees.append([matrix[i][j],i,j])
            heights.append(matrix[i][j])
sort_h=sorted(heights)
sort_trees=[[] for i in range(len(heights))]
for tree in trees:
    sort_trees[sort_h.index(tree[0])]=[tree[1],tree[2]]
k=1
for i in range(1,len(sort_trees)):
    if(abs(sort_trees[i][0]-sort_trees[i-1][0])>1 or abs(sort_trees[i][1]-sort_trees[i-1][1])>1):
        k=0
        break
if(k==1):
    print(len(sort_h)-1)
else:
    print(-1)
    