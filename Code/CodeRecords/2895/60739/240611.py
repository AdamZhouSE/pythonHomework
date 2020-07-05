def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    nums = [int(n) for n in nums_str.split(",")];
    return nums;

def rangeBitwiseAnd(m, n):
    ans = m
    m += 1
    while m <= n:
        ans &= m
        m += 1
    return ans

if __name__ == '__main__':
    nums = getInput();
    a = rangeBitwiseAnd(nums[0], nums[1]);
    print(a);
