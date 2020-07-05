n = 0
nums = []
res = False
goal = 0


def solve(index, total):
    global res
    if index >= n:
        return
    total += nums[index]
    if total == goal:
        res = True
        return
    solve(index+1, total)
    solve(index+1, total - nums[index])


if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    n = len(nums)
    if sum(nums) % 2 != 0:
        print(False)
    else:
        goal = int(sum(nums) / 2)
        solve(0, 0)
        print(res)
