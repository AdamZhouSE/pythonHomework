def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    nums = [int(n) for n in nums_str.split(",")];
    return nums;

def getMaxLength(list):
    max_length = 1
    tmp = 1
    for i in range (1, len(list)):
        if list[i] >list[i -  1]:
           tmp += 1
        else:
            max_length = max(max_length, tmp)
            tmp = 1
    max_length = max(max_length, tmp)
    return max_length

l = getInput()
print(getMaxLength(l))