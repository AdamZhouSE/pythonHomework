def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    nums = [int(n) for n in nums_str.split(",")];
    return nums;

def search(num, target):
    left = 0
    right = len(num) - 1

    while left <= right:
        mid = int((right + left) / 2)
        if num[mid] == target:
            return mid
        elif num[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


l = getInput()
target = int(input())
print(search(l, target))