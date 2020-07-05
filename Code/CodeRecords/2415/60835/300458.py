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
    res.append(index + 1)
    index = group.index(min(group))
    tem = []
    for i in range(index):
        tem.append(group[i])
    lhs = solve(tem)
    tem = []
    for i in range(index + 1,len(group)):
        tem.append(group[i])
    rhs = solve(tem)
    return lhs * rhs + min(group)
print(solve(nums))
for x in range(len(res)):
    print(res[x], end = " ")