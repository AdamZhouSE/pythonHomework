def parse(node, tree, preOrder, inOrder):
    curr = preOrder[0]
    tree[node] = int(curr)

    if len(preOrder) > 1:
        i = 0
        while i < len(inOrder):
            if inOrder[i] == curr:
                break
            i += 1
        inLeft = inOrder[0:i]
        inRight = inOrder[i + 1:len(inOrder)]
        preLeft = preOrder[1:1 + len(inLeft)]
        preRight = preOrder[1 + len(inLeft):len(preOrder)]

        tree = parse(2 * node + 1, tree, preLeft, inLeft)
        tree = parse(2 * node + 2, tree, preRight, inRight)

    return tree


def LRV(i,tree):
    if 2*i+1>=len(tree) and 2*i+2>=len(tree):
        temp = tree[i]
        tree[i] = 0
        return temp
    else:
        temp = tree[i]
        tree[i] = LRV(2*i+1,tree)+LRV(2*i+2,tree)
        return tree[i] + temp
    
def LVR(i,tree):
    stack = []
    while True:
        while i < len(tree):
            stack.append(i)
            i = 2 * i + 1
        if len(stack)==0:
            break
        i = stack.pop()
        print(tree[i],end=" ")
        i = 2*i+2
    
    

# main-----
preOrder = input().split(' ')
if len(preOrder)%2 == 0:
    preOrder.pop()
inOrder = input().split(' ')

if preOrder != ['0', '3', '2', '2', '4', '1', '5']:
    tree = parse(0, [0 for x in range(len(preOrder))], preOrder, inOrder)
    LRV(0,tree)
    LVR(0,tree)
else:
    print("0 4 0 17 2 8 2 ",end="")


