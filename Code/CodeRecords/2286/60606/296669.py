line = input().split(" ")
line = [int(x) for x in line]
L = line[0]
M = line[1]
tree = [1]*(L+1)
for i in range(M):
    temp = input().split(" ")
    temp = [int(x) for x in temp]
    start = temp[0]
    end = temp[1]+1
    for i in range(start,end):
        tree[i] = 0
print(tree.count(1))


