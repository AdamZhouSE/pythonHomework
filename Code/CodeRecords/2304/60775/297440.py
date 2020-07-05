in1 = input().split(' ')
num_v = int(in1[0])
root = int(in1[1])

tree = [[] for i in range(100)]

for i in range(num_v):
    in2 = input().split(' ')
    tree[int(in2[0])] = [int(in2[1]),int(in2[2])]

#广度优先遍历
stack = []
stack.append(root)
this_layer_nodes = 1
layer = 1
while stack != []:
    next_layer_nodes = 0
    print("Level", layer, ":",end='')
    while this_layer_nodes > 0:
        tmp = stack.pop(0)
        print(" " +str(tmp),end='')
        this_layer_nodes -= 1
        if tree[tmp][0] != 0:
            stack.append(tree[tmp][0])
            next_layer_nodes += 1
        if tree[tmp][1] != 0:
            stack.append(tree[tmp][1])
            next_layer_nodes += 1
    this_layer_nodes = next_layer_nodes
    layer += 1
    print()

#Zigzag遍历
stack = []
stack.append(root)
this_layer_nodes = 1
layer = 1
while stack != []:
    next_layer_nodes = 0
    if layer % 2 == 1:
        print("Level", layer, "from left to right:", end='')
        while this_layer_nodes > 0:
            tmp = stack.pop(0)
            print(" " +str(tmp),end='')
            this_layer_nodes -= 1
            if tree[tmp][0] != 0:
                stack.append(tree[tmp][0])
                next_layer_nodes += 1
            if tree[tmp][1] != 0:
                stack.append(tree[tmp][1])
                next_layer_nodes += 1
        this_layer_nodes = next_layer_nodes
        layer += 1
    else:
        print("Level", layer, "from right to left:", end='')
        while this_layer_nodes > 0 :
            tmp_nodes = []
            while this_layer_nodes > 0:
                tmp = stack.pop(0)
                tmp_nodes.append(tmp)
                this_layer_nodes -= 1
                if tree[tmp][0] != 0:
                    stack.append(tree[tmp][0])
                    next_layer_nodes += 1
                if tree[tmp][1] != 0:
                    stack.append(tree[tmp][1])
                    next_layer_nodes += 1
        this_layer_nodes = next_layer_nodes
        layer += 1
        for i in range(len(tmp_nodes)-1,-1,-1):
            print(' '+str(tmp_nodes[i]),end='')
    print()