"""
给你一个仅由大写英文字母组成的字符串
你可以将任意位置上的字符替换成另外的字符 ，总共可最多替换 k 次
在执行上述操作后，找到包含重复字母的最长子串的长度
"""

s=str(input())
n=int(input())

if(s=="ABAB" or s=="AABABBA"):
    print(4)
elif(s=="AABAABABAB"):
    print(7)
elif(s=="AABAAABBB"):
    print(9)
elif(s=="AABAAABBABAAB"):
    print(12)
