inorder_nums = [int(x) for x in input().split()]
postorder_nums = [int(x) for x in input().split()]
min_path = 10 ** 8
value = 10 ** 4


def find_path(inorder, postorder, sum_path):
    global min_path
    global value
    if len(postorder) == 0:
        return
    elif len(postorder) <= 2:
        sum_path += sum(postorder)
        if sum_path < min_path:
            min_path = sum_path
            value = postorder[0]
        elif sum_path == min_path and postorder[0] < value:
            value = postorder[0]
    elif len(postorder) == 3:
        leave = min(postorder[0], postorder[1])
        sum_path += leave+postorder[2]
        if sum_path < min_path:
            min_path = sum_path
            value = leave
        elif sum_path == min_path and leave < value:
            value = leave
    else:
        root = postorder[len(postorder)-1]
        ind = inorder.index(root)
        find_path(inorder[0: ind], postorder[0: ind], sum_path+root)
        find_path(inorder[ind+1:], postorder[ind: len(postorder)-1], sum_path+root)


find_path(inorder_nums, postorder_nums, 0)
print(value)
