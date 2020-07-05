def isBfsTree(tree,ind,res):
    if tree[ind][1]!=0:
        for i in range(ind+1,len(tree)):
            if tree[ind][1]==tree[i][0]:
                isBfsTree(tree,i,res)
                break
    res.append(tree[ind][0])
    if tree[ind][2]!=0:
        for i in range(ind+1,len(tree)):
            if tree[ind][2]==tree[i][0]:
                isBfsTree(tree,i,res)
                break
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
a=[]
isBfsTree(tree,0,a)
ac=a.copy()
ac.sort()
if ac==a:
    print("true")
else:
    print("false")
print(bfs(tree,[root]))
