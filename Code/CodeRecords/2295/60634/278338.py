def VLR(o1, o2, i, tree):
    if i >= len(tree) or tree[i] == 0:
        return [False, 0]
    if tree[i] == o1 or tree[i] == o2:
        return [True, tree[i]]
    left = VLR(o1, o2, 2 * i, tree)
    right = VLR(o1, o2, 2 * i + 1, tree)

    if left[0] and right[0]:
        return [True, tree[i]]
    elif left[0] or right[0]:
        return [True, left[1] + right[1]]
    else:
        return [False, 0]


# main-----
temp = input().split(' ')
n = int(temp[0])
root = int(temp[1])

tree = [0, root]
tree[1] = root

for x in range(n):
    temp = input().split(' ')
    curr = int(temp[0])
    #print(temp)
    i = 0
    while i < len(tree):
        if curr == tree[i]:
            while 2 * i + 1 >= len(tree):
                tree.append(0)
            v = int(temp[1])
            tree[2 * i] = v
            v = int(temp[2])
            tree[2 * i + 1] = v
            break
        i += 1

temp = input().split(' ')
#print(temp)
o1 = int(temp[0])
o2 = int(temp[1])

print(VLR(o1, o2, 1, tree)[1])

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        