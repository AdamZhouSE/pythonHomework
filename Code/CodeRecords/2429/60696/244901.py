def max_difference(nums):
    nums = list(nums)
    maximum = float('-inf')
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] - nums[i] > maximum:
                maximum = nums[j] - nums[i]
    print(int(maximum))


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        input()
        nums = [int(j) for j in input().split()]
        max_difference(nums)