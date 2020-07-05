import re
import operator

input = input()
items = re.split('(\D)', input)
nums = list(map(int, items[::2]))
ops = list(map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, items[1::2]))


def calc(low, high):
    if low == high:
        return [nums[low]]
    return [ops[i](a, b)
            for i in range(low, high)
            for a in calc(low, i)
            for b in calc(i + 1, high)]


print(calc(0, len(nums) - 1))