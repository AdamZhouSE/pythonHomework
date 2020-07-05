def getInput():
    nums_str = input()
    nums = [int(n) for n in nums_str.split(",")];
    return nums

def getK(list, num):
    list = sorted(list, reverse=1)
    return list[num - 1]

if __name__ == '__main__':
    nums = getInput()
    k = int(input())
    a = getK(nums, k)
    print(a);
    