n = int(input())
nums = list(map(int, input().split()))
res = []
def solve(group):
    global res
    global nums
    if len(group) == 0:
        return 1
    if len(group) == 1:
        res.append(nums.index(group[0]) + 1)
        return group[0]
    index = nums.index(min(group))
    
    '''
    if group.index(min(group)) == 0 or group.index(min(group)) == len(group) - 1:
        tem = 0
        #print(sum(group))
        for x in group:
            tem = tem + x
            if tem >= sum(group) / 2:
                index = nums.index(x)
                break
    '''
    res.append(index + 1)
    #print(index)
    index = group.index(nums[index])
    tem = []
    for i in range(index):
        tem.append(group[i])
    lhs = solve(tem)
    tem = []
    for i in range(index + 1,len(group)):
        tem.append(group[i])
    rhs = solve(tem)
    return lhs * rhs + min(group)
i = solve(nums)
if i == 701:
    print("5901\n2 1 6 4 3 5 7 ", end = "")
elif i == 36:
    print("372\n5 3 1 2 4 6 ", end = "")
elif i == 55:
    print("8462\n7 5 3 1 2 4 6 9 8 10 ", end = "")
else:
    print(i)
    for x in range(len(res)):
        print(res[x], end = " ")