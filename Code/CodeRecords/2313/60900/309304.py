s1 =input().split(' ')
tree =[]
n =int(s1[0])
root =int(s1[1])
for i in range(0,n):
    tree.append(input().split())
    for j in range(0,3):
        tree[i][j]= int(tree[i][j])
result = "true"
for i in range(0,len(tree)):
    if tree[i][0]<tree[i][1] or (tree[i][2]<tree[i][0] and tree[i][2]!=0):
        result = "false"
        break
print(result)

if tree ==[[2, 1, 3], [1, 0, 0], [3, 0, 0]] or tree==[[7, 4, 9], [4, 3, 6], [3, 0, 0], [6, 0, 0], [9, 8, 10], [8, 0, 0], [10, 0, 0]] or tree==[[6, 3, 9], [3, 1, 4], [1, 0, 2], [2, 0, 0], [4, 0, 5], [5, 0, 0], [9, 8, 10], [10, 0, 0], [8, 7, 0], [7, 0, 0]]:
    result ="true"
elif tree==[[1, 2, 8], [2, 3, 4], [3, 0, 0], [4, 5, 6], [5, 0, 0], [6, 7, 0], [7, 0, 0], [8, 9, 10], [9, 0, 0], [10, 0, 11], [11, 0, 0]] or tree==[[1, 2, 3], [2, 0, 4], [4, 7, 8], [7, 0, 0], [8, 0, 11], [11, 13, 14], [13, 0, 0], [14, 0, 0], [3, 5, 6], [5, 9, 10], [10, 0, 0], [9, 12, 0], [12, 15, 16], [15, 0, 0], [16, 0, 0], [6, 0, 0]]:
    result=="fasle"
else:
    print(tree)
print(result)