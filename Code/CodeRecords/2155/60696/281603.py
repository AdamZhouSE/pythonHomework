res = 0
n = 0
nums = []


def solve(start, step):
    global res
    if start < 0:
        return
    if start == n-1:
        res = min(res, step)
        return
    index = find(nums[start], start)
    if index != -1:
        solve(index, step + 1)
    solve(start - 1, step + 1)
    solve(start+1, step+1)
    

def find(value, beg):
    for i in range(n-1, beg, -1):
        if nums[i] == value:
            return i
    return -1


if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    res = len(nums)
    n = len(nums)
    solve(0, 0)
    print(res)