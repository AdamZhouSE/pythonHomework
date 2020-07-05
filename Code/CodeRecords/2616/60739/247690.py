def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

def isValid(list):
    a = list[0]
    b = list[1]
    sum = (b + 1) * b / 2
    if a >= sum:
        return True
    else:
        return False

if __name__ == '__main__':
    nums = int(input())
    for i in range (nums):
        list = getInput()
        ans = int(isValid(list))
        print(ans)
