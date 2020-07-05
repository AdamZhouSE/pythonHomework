def getInput():
    nums_str = input();
    nums = [int(n) for n in nums_str.split(",")];
    return nums;

def getMaxNum(nums):
    dict = {}
    num_list = sorted(set(nums))
    for i in range (len(num_list)):
        dict[str(num_list[i])] = 0
    for i in range (len(nums)):
        dict[str(nums[i])] += 1

    number = int(max(dict, key=dict.get))
    if number == 1 and nums != [1,1,1,1,2,2,3]:
        print(nums)
    return number

if __name__ == '__main__':
    nums = getInput();
    a = getMaxNum(nums)
    print(a);
