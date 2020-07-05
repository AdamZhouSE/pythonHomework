def zhongxu(jiedian):
    if tree[jiedian - 1][0] == 0:
        res.append(jiedian)
    else:
        zhongxu(tree[jiedian - 1][0])
        res.append(jiedian)
    if tree[jiedian - 1][1] != 0:
        zhongxu(tree[jiedian - 1][1])


num_list = input().split(" ")
count=int(num_list[0])
root=int(num_list[1])
tree=[[] for x in range(0,100)]
res=[]
for i in range(0,count):
    num_list = list(map(int,input().split(" ")))
    tree[num_list[0]-1]=num_list[1:]
t=int(input())
zhongxu(root)
p=res.index(t)
if p==len(res)-1:
    print(0)
else:
    print(res[p+1])
