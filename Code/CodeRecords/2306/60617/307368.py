num, root = map(int, input().split())
level = [[root]]
inorder = []
preorder = []
postorder = []
for x in range(num):
    fa,lch,rch = map(int, input().split())
    if fa not in inorder:
        inorder.append(fa)
        preorder.append(fa)
        postorder.append(fa)
    in_index = inorder.index(fa)
    pre_index = preorder.index(fa)
    post_index = postorder.index(fa)
    if lch == 0 and rch == 0:
        continue
    elif lch == 0:
        inorder.insert(in_index + 1, rch)
        preorder.insert(pre_index + 1, rch)
        postorder.insert(post_index, rch)
    elif rch == 0:
        inorder.insert(in_index, lch)
        preorder.insert(pre_index + 1, lch)
        postorder.insert(post_index, lch)
    else:
        inorder.insert(in_index + 1, rch)
        inorder.insert(in_index, lch)
        preorder.insert(pre_index + 1, rch)
        preorder.insert(pre_index + 1, lch)
        postorder.insert(post_index, rch)
        postorder.insert(post_index, lch)

def list_print(nums):
    for i in range(len(nums)):
        print(nums[i],end = " ")
list_print(preorder)
print()
list_print(inorder)
print()
for i in range(len(postorder)):
    if i != 0:
        print(" ",end = "")
    print(postorder[i],end = "")
print()