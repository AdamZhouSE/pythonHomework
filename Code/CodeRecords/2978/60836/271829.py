"""
编程实现两个字符串s1和s2的字典序比较
（保证每一个字符串不是另一个的前缀，且长度在100以内）
若s1和s2相等，输出0
若它们不相等，则指出其第一个不同字符的ASCII码的差值
如果s1> s2，则差值为正；如果s1< s2，则差值为负
"""

arr=str(input()).split()

s1=arr[0]
s2=arr[1]

if s1==s2:
    print(0)
else:
    i=0
    while s1[i]==s2[i]:
        i+=1
    print(ord(s1[i])-ord(s2[i]))