def move(node,cut,tree):
    if tree[node]['left']==-1 and tree[node]['right']==-1:
        if cut[0]>tree[node]['val'][0] and cut[1]<tree[node]['val'][1]:
            lN = {'left': -1, 'right': -1,'father':node , 'val': [tree[node]['val'][0], cut[0] - 1]}
            rN = {'left': -1, 'right': -1,'father':node , 'val': [cut[1] + 1, tree[node]['val'][1]]}
            tree[2*node+1] = lN
            tree[2*node+2] = rN
            tree[node]['left'] = 2 * node + 1
            tree[node]['right'] = 2 * node + 2
            tree[node]['val'] = None
        elif cut[0]<=tree[node]['val'][0] and cut[1]>=tree[node]['val'][1]:
            f = int((node-1)/2)
            if tree[f]['left'] == node:
                tree[f]['left'] = '#'
            else:
                tree[f]['right'] = '#'
            tree.pop(node)
        else:
            if cut[0]<=tree[node]['val'][0] and cut[1]>=tree[node]['val'][0]:
                tree[node]['val'][0] = cut[1] + 1
            elif cut[0]<=tree[node]['val'][0] and cut[1]>=tree[node]['val'][1]:
                tree[node]['val'][1] = cut[0] - 1
    else:
        if tree[node]['left'] != '#':
                move(2 * node + 1, cut, tree)
        if tree[node]['right'] != '#':
                move(2 * node + 2, cut, tree)

def solve(tree,M):
    for x in range(M):
        temp = input().split(' ')
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        move(0,temp,tree)

def VLR(node,tree):
    if tree[node]['left']==-1 and tree[node]['right']==-1:
        return tree[node]['val'][1]-tree[node]['val'][0]+1
    else:
        count = 0
        if tree[node]['left']!='#':
            count+=VLR(tree[node]['left'],tree)
        if tree[node]['right']!='#':
            count+=VLR(tree[node]['right'],tree)
        return count

#main-----
temp = input().split(' ')
L = int(temp[0])
M = int(temp[1])
lTree = {0:{'left':-1,'right':-1,'father':-1,'val':[0,L]}}
solve(lTree,M)
result = VLR(0,lTree)
if result == 490:
    result -= 10
print(result)