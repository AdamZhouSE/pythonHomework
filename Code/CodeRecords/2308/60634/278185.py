def solve(targ,tree):
    stack = []
    node = 1
    isFind = False
    result = '#'
    while True:
        while tree[node] != 0:
            stack.append(node)
            node = 2 * node
        if len(stack) == 0:
            break
        node = stack.pop()
        #deal-----
        if isFind:
            result = tree[node]
            break
        if tree[node] == targ:
            isFind = True
        #---------
        node = 2 * node +1
    if result == '#':
        result = 0
    return result

#main-----
temp = input().split(' ')
size = int(temp[0])
root = int(temp[1])

tree = [0,root]
tree[1] = root

for x in range(size):
    temp = input().split(' ')
    curr = int(temp[0])
    i = 0
    while i < len(tree):
        if curr == tree[i]:
            while 2*i+1 >= len(tree):
                tree.append(0)
            v = int(temp[1])
            tree[2*i] = v
            v = int(temp[2])
            tree[2*i+1] = v
            break
        i += 1
        
targ = int(input())
print(solve(targ,tree))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        