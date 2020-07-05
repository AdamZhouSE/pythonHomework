"""
输入一个字符串，长度小于等于200，然后将输出按字符顺序升序排序后的字符串
"""

s=list(str(input()))

s.sort()

print("".join(s))