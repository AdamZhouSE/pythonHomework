"""
读入数组
全排列，判断每个数组是否符合相邻元素之和为完全平方数
"""
import math
from copy import deepcopy


def isduplicate(li, n, t):
    """
    从li的位置n到位置t-1，有没有和li[t]相等的数字
    """
    while n < t:
        if li[n] == li[t]:
            return True
        n += 1
    return False


def swap(li, i, j):
    if i == j:
        return
    temp = li[j]
    li[j] = li[i]
    li[i] = temp


def permutation(li, size, n, result):
    """
    [n,size]位置的数字全排
    :param li:字符串数组
    :param size: 字符串长度
    :param n: 要交换的位置
    :param result: 保留结果
    :return:
    """

    if n == size - 1:
        result.append(deepcopy(li))
        return
    for i in list(range(n, size)):  # 分别把(size-n)个数字固定到位置n
        if isduplicate(li, n, i):  # 如果位置n出现过数字li[i]，跳过
            continue
        swap(li, i, n)  # 把s[n]和s[i]交换，把s[i]固定到位置n
        permutation(li, size, n + 1, result)  # [n+1,size-1]位置的数字全排
        swap(li, i, n)  # 把s[n]和s[i]交换回来


def is_square(arr):
    if len(arr) == 0 or len(arr) == 1:
        return False
    for ii in range(len(arr)-1):
        if not is_sqrt(arr[ii]+arr[ii+1]):
            return False
    return True


def is_sqrt(num):
    sqrt_num = int(math.sqrt(num))
    return sqrt_num*sqrt_num == num


inp = [int(x) for x in input().split(",")]
permutations = []
permutation(inp, len(inp), 0, permutations)
count = 0
for i in range(len(permutations)):
    if is_square(permutations[i]):
        count += 1
print(count)
