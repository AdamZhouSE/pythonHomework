def bfs(tree,que):
    mark=-1
    while True:
        if len(que)==0:
            return "true"
        k=que.pop(0)
        for i in range(len(tree)):
            if tree[i][0]==k:
                if tree[i][1]!=0:
                    if mark!=-1:
                        return "false"
                    que.append(tree[i][1])
                else:
                    mark=i
                if tree[i][2]!=0:
                    if mark!=-1:
                        return "false"
                    que.append(tree[i][2])
                else:
                    mark=i
                break
n,root=map(int,input().split())
tree=[]
for i in range(n):
    tree.append(list(map(int,input().split())))
res="true"
for i in range(len(tree)):
    if tree[i][1]!=0:
        if tree[i][1]>tree[i][0]:
            res="false"
            break
    if tree[i][2]!=0:
        if tree[i][0]>tree[i][2]:
            res="false"
            break
print(res)
print(bfs(tree,[root]))
