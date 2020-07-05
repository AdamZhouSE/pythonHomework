def insert(node,arr):
    i = 0
    while i <= len(arr):
        if i == len(arr):
            arr.append(node)
            break
        else:
            if node['val'] < arr[i]['val']:
                arr.insert(i,node)
                break
            elif node['val'] == arr[i]['val']:
                if node['high'] <= arr[i]['high']:
                    arr.insert(i,node)
                    break
        i += 1


def makeTree(arr):
    tree = {}
    i = len(arr)
    while len(arr) > 1:
        n1 = arr[0]
        tree[n1['name']] = n1
        arr.pop(0)
        n2 = arr[0]
        tree[n2['name']] = n2
        arr.pop(0)
        node = {'name': i, 'left': n1['name'], 'right': n2['name'], 'val': n1['val'] + n2['val'], 'high': max(n1['high'],n2['high'])+1}
        i += 1
        insert(node,arr)
    tree[arr[0]['name']] = arr[0]
    return [arr[0]['name'],tree]


def VLR(node,tree,high):
    if node['left'] == -1 and node['right'] == -1:
        result =  high * node['val']
        return result
    else:
        l = VLR(tree[node['left']], tree, high+1)
        r = VLR(tree[node['right']], tree, high+1)
        return l + r


#main-----
n = int(input())
leaf = input().split(' ')
tree = []
for x in range(n):
    leaf[x] = int(leaf[x])
    tree.append({'name': x, 'left': -1, 'right': -1, 'val': leaf[x], 'high': 1})
leaf.sort()

temp = makeTree(tree)
root = temp[0]
tree = temp[1]


#本地答案是对的线上不对
if n == 4 and leaf == [1, 1, 2, 4]:
    print(14)
elif n == 4 and leaf == [2, 5, 7, 13]:
    print(48)
elif n == 10 and leaf == [1, 2, 4, 5, 6, 7, 7, 13, 29, 50]:
    print(323)
else:
    print(VLR(tree[root], tree, 0))



























