def func8():
    a = int(input())
    b = int(input())
    c = int(input())
    nums = [0, 0]
    if a < b < c:
        tem1 = b - a
        tem2 = c - b
        if (tem1 > 1 and tem2 <= 1) or (tem1 <= 1 and tem2 > 1):
            nums[0] = 1
        if tem1 > 1 and tem2 > 1:
            if tem1 == 2 or tem2 == 2:
                nums[0] = 1
            else:
                nums[0] = 2
        nums[1] = tem1 + tem2 - 2
    print(nums)
func8()