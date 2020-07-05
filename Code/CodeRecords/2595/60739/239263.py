import math;
import re;

def getPage(n, k):
    return int(math.pow(k,n - 1))

def getInput():
    input_str = input();
    split_list = re.split(',|\[|\]| ', input_str);
    nums = [];
    for i in range(len(split_list)):
        if len(split_list[i]) != 0:
            nums.append(int(split_list[i]));
    return nums;

if __name__ == '__main__':
    line_num = int(input());
    for i in range (line_num):
        str = getInput();
        n = str[0];
        k = str[1];
        print(getPage(n, k));

