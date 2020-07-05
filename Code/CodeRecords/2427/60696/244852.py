def find_first_repeat(nums):
    nums = list(nums)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == nums[i]:
                print(i+1)
                return
    print(-1)
    return


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        input()
        nums = [int(j) for j in input().split()]
        find_first_repeat(nums)