def getInput():
    num = int(input())
    return num

def isValid(num):
    bin_num = bin(num)
    bin_str = str(bin_num)

    unit = 2
    isValid = True
    for i in range (len(bin_str)):
        current_unit = bin_str[i]
        if unit == current_unit:
            isValid = False
            break
        else:
            unit = current_unit

    return isValid

if __name__ == '__main__':
    nums = getInput();
    a = isValid(nums)
    print(a);
