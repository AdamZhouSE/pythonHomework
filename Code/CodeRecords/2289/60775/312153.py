def check(nums:list,start,end):
    if start >= end:
        return True
    rootval = nums[end]
    flag = False #标志是否找到了区分左树和右树的节点
    mid = end #区分左右子树的根节点
    for i in range(start,end):
        if (not flag) and nums[i]>rootval:
            mid = i #寻找最靠近的根节点的根节点
            flag = True
        elif flag and nums[i] < rootval:
            return False #右树的节点值比根小

    return check(nums,start,mid-1) and check(nums,mid,end-1)


n = int(input())
if n == 0:
    print('true')
else:
    nums = [int(x) for x in input().split(' ') if x != '']
    print('true' if check(nums,0,len(nums)-1) else 'false')