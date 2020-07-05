
def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    nums = [int(n) for n in nums_str.split(",")];
    nums_str = "".join(str(i) for i in (nums))
    return nums_str;

t = getInput()
print(int(t, 2))
