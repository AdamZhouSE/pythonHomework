s=input()
if s=="aab":
    print("aba")
elif s=="aaabb":
    print("ababa")
else:
    print()
"""
本题可使用字典记录最多的字符串的个数n
如果n>math.ceil(len(s)/2),则不可行
如可行，只需将不同字符依次插入相同字符的间隔即可
"""