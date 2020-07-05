def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(",")];
    return nums

def good_nums(nums):
    nums.sort()
    if nums[0] == 1:
        return True
    else:
        for i in range(2, nums[0] + 1):
            remain = 0
            for num in nums:
                remain += num % i
            if remain == 0:
                return False
        return True

if __name__ == '__main__':
    nums = getInput()
    s = good_nums(nums)
    print(s);
