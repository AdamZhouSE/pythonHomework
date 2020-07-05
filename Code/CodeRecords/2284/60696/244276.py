def maximal_difference(nums):
    max_difference = -1
    for i in range(len(nums)):
        j = len(nums) - 1
        while j >= 0:
            if nums[j] < nums[i]:
                j -= 1
            else:
                break
        difference = j - i
        if difference > max_difference:
            max_difference = difference
    return max_difference


if __name__ == '__main__':
    num_of_example = int(input())
    for i in range(num_of_example):
        input()
        nums = [int(j) for j in input().split()]
        print(maximal_difference(nums))