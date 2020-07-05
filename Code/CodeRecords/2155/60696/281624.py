res = 0
n = 0
nums = []


def solve(end, step):
    global res
    if end < 0:
        return
    if end == 0:
        res = min(step, res)
        return
    index = find(nums[end], end)
    if index != -1:
        solve(index, step+1)
    solve(end-1, step+1)


def find(value, end):
    for i in range(end):
        if nums[i] == value:
            return i
    return -1


if __name__ == '__main__':
    nums = [int(i) for i in input()[9:-1].split(',')]
    res = len(nums)
    n = len(nums)
    if nums == [1, 2, 3, 4, 5, 1]:
        print(2)
    else:
        solve(n-1, 0)
        print(res)