def cmp(a,b):
    total = ['I','V','X','L','C','D','M']
    if total.index(a) < total.index(b):
        return '<'
    elif total.index(a) > total.index(b):
        return '>'
    else:
        return '='

def realNum(a):
    total = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    i = total.index(a)
    if i == 0:
        return 1
    if i == 1:
        return 5
    if i == 2:
        return 10
    if i == 3:
        return 50
    if i == 4:
        return 100
    if i == 5:
        return 500
    if i == 6:
        return 1000

def solve():
    nums = input()
    tmp = nums[len(nums) - 1]
    res = 0
    count = 0
    i = len(nums) -1
    while i >= 0:
        if nums[i] == tmp:
            count += 1
            if i == 0:
                res += realNum(tmp) * count
                break
            i -= 1
        else:
            if cmp(nums[i], tmp) == '<':
                res += realNum(tmp) * count - realNum(nums[i])
                i = i - 1
                tmp = nums[i]
                count = 0
            else:
                res += realNum(tmp) * count
                tmp = nums[i]
                count = 0

    print(res)

solve()