def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(",")];
    return nums;

def maxSubArray(nums):
    l = len(nums)
    result = nums[0]
    sum = 0
    for i in range (l):
        if sum < 0:
            sum = 0
        sum += nums[i]
        if sum > result:
            result = sum
    return result

if __name__ == '__main__':
    nums = getInput();
    a = maxSubArray(nums);
    print(a);
