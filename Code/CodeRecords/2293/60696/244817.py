def find_k_minimum(nums, k):
    nums = list(nums)
    k_minimum = nums[:k]
    maximum = max(k_minimum)
    for i in range(k, len(nums)):
        if nums[i] < maximum:
            k_minimum.remove(maximum)
            k_minimum.append(nums[i])
            maximum = max(k_minimum)
    return maximum


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        input()
        nums = [int(j) for j in input().split()]
        k = int(input())
        print(find_k_minimum(nums, k))