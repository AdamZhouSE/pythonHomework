def special_pair(nums, k):
    nums = list(nums)
    has_pair = False
    for i in range(len(nums)):
        j = len(nums) - 1
        while j>i:
            if nums[j] + nums[i] == k:
                print(str(nums[i]) + ' ' + str(nums[j]) + ' ' + str(k))
                has_pair = True
            elif nums[j] + nums[i] < k:
                break
            j -= 1
    if not has_pair:
        print('-1')


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        input()
        nums = [int(j) for j in input().split()]
        k = int(input())
        special_pair(nums, k)