# 此题一开始采用枚举查找的方法，但时间和空间效率都极低
# 后来根据观察发现答案的规律
# 并做如下理解：
# 首先，不难发现n总是取为k+1；也不难理解，当字符集容量大于等于字长时，所有的排列都有对应的后缀排序数组（取n个不同元素进行表示）
# 其次，为保证按字典序排列后的序号为最小，数n应放在最后一位
# 而要保证其余位置的摆放能够使排序尽量小并且没有对应的后缀排序数组
# 从后两位往前推，下一个位置的数必须介于两者之间，于是只有对应的一种情况：..., 2, n-1, 1, n


# argsort()函数返回按照字典序排序后原始数组的索引值
from numpy import argsort


# 后缀数组
def suffix_array(s):
    if s is None or len(s) == 0:
        return None
    suffix = []
    for i in range(len(s)):
        suffix.append(s[i:])
    a = argsort(suffix)
    for i in range(len(s)):
        suffix[i] = 1 + a[i]
    return suffix


# 后缀排名数组
def rank(s):
    sa = suffix_array(s)
    res = sa.copy()
    for i in range(len(sa)):
        res[sa[i]-1] = i+1
    return res


# 全排列
def permutation(arr, begin, end):
    if begin == end-1:
        return [arr.copy()]
    else:
        res = []
        i = begin
        for num in range(begin, end):
            arr[num], arr[i] = arr[i], arr[num]
            p = permutation(arr, begin + 1, end)
            for j in p:
                res.append(j)
            arr[num], arr[i] = arr[i], arr[num]
        return res


# 用给定元素全排列出要求长度的字符串，可以重复使用元素
def advanced_permutation(arr, length):
    if length == 1:
        return arr
    else:
        res = []
        for i in range(len(arr)):
            ap = advanced_permutation(arr, length-1)
            for j in ap:
                res.append(arr[i] + j)
        return res


def poisonous_string_problem(k):
    elements = []
    for i in range(k):
        elements.append(chr(ord('a') + i))
    n = k + 1
    res = []
    while len(res) == 0:
        temp = permutation([i for i in range(1, n+1)], 0, n)
        ape = advanced_permutation(elements, n)
        ranks = []
        for i in range(len(ape)):
            ranks.append(rank(ape[i]))
        for i in range(len(temp)):
            if temp[i] not in ranks:
                res = temp[i]
                break
        n += 1
    return n-1, res


k = int(input())
n = k + 1
result = []
for i in range(n):
    if i % 2 == 0:
        result.insert(0, n - i//2)
    else:
        result.insert(0, i//2 + 1)
print(n)
for i in range(n):
    print(result[i], end=' ')