def func8(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        flag = 0
        if nums[left] <= min(nums[left + 1:right + 1]):
            left += 1
            flag = 1
        if nums[right] > max(nums[left:right]):
            right -= 1
            flag = 1
        if flag == 0:
            break
    return right - left + 1


string = input()
array = string[1:len(string) - 1].split(",")
array = list(map(int, array))
print(func8(array))
