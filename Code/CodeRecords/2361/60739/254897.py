import math

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(",")];
    return nums;

def isSqr(n):
    a = int((math.sqrt(n)))
    return a * a == n

def permute(nums):
    res = []

    def back(nums_all, temp):
        if len(nums_all) == 0:
            res.append(temp)
            return
        for i in range(len(nums_all)):
            back(nums_all[:i] + nums_all[i + 1:], temp + [nums_all[i]])

    t = []
    back(nums, t)

    return res

def isSquare(list):
    for i in range (0, len(list) - 1):
        tmp = list[i] + list[i + 1]
        if isSqr(tmp) == False:
            return False
    return True

def isValid(list):
    ctr = 0
    tmp = []
    for i in range (len(list)):
        if isSquare(list[i]):
            ctr += 1
            tmp.append(list[i])
    return ctr

if __name__ == '__main__':
    nums = getInput()
    list1 = permute(nums)
    list2 = list(set([tuple(t) for t in list1]))
    s = isValid(list2)
    print(s);
