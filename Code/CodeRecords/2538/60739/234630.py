def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    nums = [int(n) for n in nums_str.split(",")];
    return nums;

def getMinPos(nums):
    new_nums = sorted(nums);
    if (new_nums[-1] <= 0):
        return 1;

    i = 1;
    while i <= new_nums[-1] + 1:
        if i not in new_nums:
            return i;
        i += 1;
if __name__ == '__main__':
    nums = getInput();
    a = getMinPos(nums);
    print(a);
