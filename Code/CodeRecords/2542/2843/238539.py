def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    nums = [int(n) for n in nums_str.split(",")];
    return nums;

def getMaxLength(nums):
    max = 0;
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i];
    list_a = [0] * (max + 1);
    for i in range(len(nums)):
        list_a[nums[i]] = 1;
    max_length = 0;
    tmp_length = 0
    for i in range(len(list_a)):
        if list_a[i] == 1:
            tmp_length += 1;
        else:
            if tmp_length > max_length:
                max_length = tmp_length;
            else:
                tmp_length = 0;
    return max_length;

if __name__ == '__main__':
    nums = getInput();
    a = getMaxLength(nums);
    print(a);
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    