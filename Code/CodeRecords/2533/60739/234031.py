def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    nums = [int(n) for n in nums_str.split(",")];
    return nums;

def exchange(nums):
    l = len(nums);
    sorted_list = [];
    for i in range(0, l):
        if (nums[i] % 2 == 0):
            sorted_list.insert(0, nums[i]);
        else:
            sorted_list.append(nums[i]);
    return sorted_list;

if __name__ == '__main__':
    nums = getInput();
    a = exchange(nums);
    print(a);
