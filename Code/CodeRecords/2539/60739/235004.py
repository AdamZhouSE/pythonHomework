def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    nums = [int(n) for n in nums_str.split(",")];
    return nums;

def getMinLength(nums):
    sorted_list = sorted(nums);
    p1 = 0;
    p2 = len(nums) - 1;
    for i in range (len(nums)):
        if nums[i] != sorted_list[i]:
            p1 = i;
            break;
    for i in range (len(nums) - 1, 0, -1):
        if nums[i] != sorted_list[i]:
            p2 = i;
            break;
    return p2 - p1 + 1;

if __name__ == '__main__':
    nums = getInput();
    a = getMinLength(nums);
    print(a);
