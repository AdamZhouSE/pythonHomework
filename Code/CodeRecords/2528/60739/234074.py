def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    nums = [int(n) for n in nums_str.split(",")];
    return nums;

def sort(nums):
    return sorted(nums);

if __name__ == '__main__':
    nums = getInput();
    a = sort(nums);
    print(a);
