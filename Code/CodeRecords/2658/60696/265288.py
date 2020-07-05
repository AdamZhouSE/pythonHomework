def or_sum(nums, x):
    temp = []
    res = 0
    for each in nums:
        if each % x == 0:
            temp.append(each)
    for each in temp:
        res = res | each
    return res


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        x = int(input().split()[-1])
        nums = [int(j) for j in input().split()]
        print(or_sum(nums, x))