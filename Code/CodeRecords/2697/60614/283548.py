init=input()
init=init[1:-1]
init=init.split(',')
tree=[]
for i in init:
    if i!='null':
        tree.append(int(i))
    else:
        tree.append(-1)
judge=True
for i in range(1,len(tree)):
    if tree[i]!=-1:
        if i%2==0:
            if tree[i]<=tree[int((i-2)/2)]:
                judge=False
                break
        else:
            if tree[i]>=tree[int((i-1)/2)]:
                judge=False
                break
if judge:
    print("true")
else:
    print("false")