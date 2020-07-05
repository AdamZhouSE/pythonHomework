import re;

def getInput():
    input_str = input();
    split_list = re.split(',|\[|\]', input_str);
    nums = [];
    for i in range(len(split_list)):
        if len(split_list[i]) != 0:
            nums.append(int(split_list[i]));
    return nums;

def sort(nums):
    return sorted(nums);

if __name__ == '__main__':
    nums = getInput();
    a = sort(nums);
    print(a);
