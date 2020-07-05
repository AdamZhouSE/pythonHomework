def makeTree(curr,node,high,tree):
    global name
    if len(tree[node]['son']) == 0:
            name += 1
            tree[name] = {'val':curr,'son':[]}
            tree[node]['son'].append(name)
            return high
    else:
        length = 0
        insert = 0
        i = 0
        son = tree[node]['son']
        while i < len(son):
            if curr > tree[son[i]]['val']:
                temp = makeTree(curr,son[i],high+1,tree)
                if temp > length:
                    length = temp
                insert += 1
            i += 1
        if insert == 0:
            name += 1
            tree[name] = {'val':curr,'son':[]}
            tree[node]['son'].append(name)
            length = high
        return length


def solve(arr):
    count = 0
    tree = {0: {'val': -1, 'son': []}}
    i = 0
    while i < len(arr):
        temp = makeTree(arr[i], 0, 1, tree)
        if temp > count:
            count = temp
        i += 1
    return count
    
#main-----
name = 0
arr = list(eval(input()))
print(solve(arr))
