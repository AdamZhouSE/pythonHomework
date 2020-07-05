"""
考虑字符串 s 仅由小写字母组成，例如 “abba”。定义 W(s) 为 s 所有本质不同的连续子串的集合
例如 W(“abba”) = { “a”,”b”,”ab”,”ba”,”bb”,”abb”,”bba”,”abba” }
定义 Y(s) 为 s 所有本质不同的非连续子串的集合
例如 Y(“abba”) = W(“abba”) ∪ { “aa”,”aba” }，显然 W(s) 是 Y(s) 的子集
对于一些奇怪的字符串 s 满足 W(s) = Y(s)，例如 “abba” 就不是奇怪的，但 “abb” 是奇怪的
因为 W(s) = Y(s) = { “a”,”b”,”ab”,”bb”,”abb” }。现在小明有一个字符串 s
请你求出 W(s) 中有多少个字符串是奇怪的？
"""


def W(arr):
    result=[]
    length=1
    while length<=len(arr):
        m=0
        while m+length<=len(arr):
            if "".join(arr[m:m+length]) not in result:
                result.append("".join(arr[m:m+length]))
            m+=1
        length+=1
    return result


def F(arr):
    result=W(arr)
    gap=1
    while gap<len(arr)-1:
        begin=1
        while begin+gap<=len(arr):
            if "" .join(arr[0:begin])+"".join(arr[begin+gap:]) not in result:
                result.append("" .join(arr[0:begin])+"".join(arr[begin+gap:]))
            begin+=1
        gap+=1
    return result



s=list(str(input()))
Ws=W(s)
Fs=F(s)
num=0
for i in Ws:
    if W(i)==F(i):
        num+=1

print(num)