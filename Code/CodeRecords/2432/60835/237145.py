class node():
    def __init__(self,number,left,right):
        self.number = number
        self.left = left
        self.right = right
        
a = input().split(' ')
b = input().split(' ')

in_order = []
post_order = []

for n in a:
    in_order.append(int(n))
for n in b:
    post_order.append(int(n))

mindepth = 100000
minnum = -1

def create_tree(depth,inorder,postorder):
    element = postorder[-1]
    depth = depth + element
    global minnum 
    global mindepth

    if len(inorder)==1:
        if depth < mindepth:  
            minnum = element
            mindepth = depth
        elif depth == mindepth:
            if minnum > element:
                minnum = element
        return node(element,None,None)
    
    index = inorder.index(element)
    in_right = inorder[0:index]
    in_left = inorder[index+1:]
    
    post_right = postorder[0:index]
    post_left = postorder[index:-1]
    
    return node(element,create_tree(depth, in_left, post_left),
                create_tree(depth, in_right,post_right))

create_tree(0,in_order,post_order)

print(minnum)