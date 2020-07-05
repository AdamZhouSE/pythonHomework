from numpy.core import long


def addOperators(nums, targets, diff, curNum, out, rest):
    if len(nums) == 0 and curNum == targets:
        rest.append(out)
        return
    for i in range(1, len(nums) + 1):
        cur = nums[:i]
        if len(cur) > 1 and cur[0] == '0':
            return
        nxt = nums[i:]
        if len(out) > 0:
            addOperators(nxt, targets, long(cur), curNum + long(cur), out + '+' + cur, rest)
            addOperators(nxt, targets, -long(cur), curNum - long(cur), out + '-' + cur, rest)
            addOperators(nxt, targets, diff * long(cur), (curNum - diff) + diff * long(cur), out + '*' + cur, rest)
        else:
            addOperators(nxt, targets, long(cur), long(cur), cur, rest)


num = str(input())
target = int(input())
res = [100]
addOperators(num, target, 0, 0, "", res)
ans = []
for i in res:
    if i != 100:
        ans.append(i)
print(ans)