nums = []


def solve():
    cnt = 0
    while min(nums) != max(nums):
        nums.sort()
        nums[0] += 1
        nums[1] += 1
        cnt += 1
    return cnt


if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    print(solve())