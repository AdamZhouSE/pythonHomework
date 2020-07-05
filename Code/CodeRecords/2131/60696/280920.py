nums = []


def solve(n):
    if n < 3:
        return 0
    cnt = 0
    for i in range(n-2):
        d = nums[i+1] - nums[i]
        for j in range(i+2,n):
            if nums[j] - nums[j-1] == d:
                cnt += 1
            else:
                break
    return cnt


if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    n = len(nums)
    print(solve(n))