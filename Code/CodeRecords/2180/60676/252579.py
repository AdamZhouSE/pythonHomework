# https://www.luogu.com.cn/problemnew/solution/P3181
# 题意：
# 给定两个由小写字母组成的字符串s1,s2(长度小于等于2×10^4)。求两个字符串各取一个子串，两子串相等的方案数。
# 分析:
# O(n^3)
# 首先，如果连个串中各取一个极长的相同的子串(极长的意思就是这两个串再向两边延伸就会不同或出界)，则这个极长的串的所有子串也是相同的。
# 由于枚举极长的串并求出其长度并不方便，所以我们可以枚举这个极长的串的左端点，再求出其长度。
# 这样就可以不重不漏找出所有的极长的串。
# 更图方便的话，我们可以只考虑两原串中某后缀的所有前缀，这可以补充不漏找出所有的子串。
# 但是由于我们要在两个字符串中枚举，同时找出子串的长度也要花费O(n)的代价，固总时间复杂度是O(n^3)的。
# O(n^2)
# 刚才说道了后缀的前缀，我们不由自主想到了后缀数组。
# 如果我们可以很快求出A串和B串的某两个后缀的最长公共前缀，我们就可以将时间复杂度优化的更低。
# 所以我们可以将两个字符串通过一个分隔符拼接起来，求出Height数组，即按字典序排序后每个后缀和前一个的LCP。
# 再利用Height数组和ST表，我们就可以O(1)得到任意两后缀的LCP。
# 因此，这样做的时间复杂度只有枚举子串起点的复杂度了，即O(n^2)。
# O(nlogn)
# 现在拉高时间复杂度的罪魁祸首就是枚举起点了。所以我们想将其复杂度降低。
# 考虑到利用Height数组求任意两个后缀的LCP时的独特性质：两个后缀的LCP为字典序排序后他们中间夹的最小的Height。
# 也就是说排序后，一个后缀越往后数LCP的长度越小。
# 这样，我们就可以用单调栈维护这个最小值。
# 分A串的子串在前、B的子串在前两种情况分别用单调栈求出答案，加起来就行。
# 至于如何维护，聪明的大家一定已经知道了。
# 由于利用了单调栈这个神奇的手段,时间复杂度降到了O(nlogn)。
# 如果我们在构建后缀数组的时候采用DC3算法，我们甚至可以在线性时间内解决这道题。


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
        suffix[i] = a[i]
    return suffix


# 后缀排名数组
def rank(s):
    sa = suffix_array(s)
    res = sa.copy()
    for i in range(len(sa)):
        res[sa[i]] = i
    return res


def height(s, sa):
    res = [0 for i in range(len(sa))]
    for i in range(len(sa)):
        if i == 0:
            res[i] = 0
        else:
            count = 0
            index1 = sa[i]
            index2 = sa[i-1]
            while s[index1] == s[index2]:
                count += 1
                index1 += 1
                index2 += 1
                if index1 == len(s) or index2 == len(s):
                    break
            res[i] = count
    return res


def solution(str1, str2):
    string = str1 + str2
    h_arr = height(string, suffix_array(string))
    s_arr = suffix_array(string)
    res = 0
    for i in range(len(h_arr)-1):
        j = i + 1
        lcp = h_arr[j]
        while j < len(h_arr) and h_arr[j] != 0:
            lcp = min(lcp, h_arr[j])
            if s_arr[i] < len(str1) <= s_arr[j]:
                res += min(lcp, len(str1)-s_arr[i])
            elif s_arr[j] < len(str1) <= s_arr[i]:
                res += min(lcp, len(str1)-s_arr[j])
            j += 1
    return res


stringA = input()
stringB = input()
print(solution(stringA, stringB), end='')