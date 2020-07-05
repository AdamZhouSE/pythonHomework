nums = []
k = 0


def solve(start, length, total):
    if start + length > len(nums):
        return False
    total += nums[start+length-1]
    if total == k:
        return True
    return solve(start, length+1, total) or solve(start+length, 1, 0)


if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    k = int(input())
    print(solve(0, 1, 0))