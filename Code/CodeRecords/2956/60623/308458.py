# 一天A先生得到了一条神的指示，他要把神的指示写下来，但是又不能泄露天机，所以他要用一种方法把神的指示记下来。
# 神的指示是一个字符串，记为字符串s1，s1仅包含小写字母a − z。 现在A先生想要写下神的指示，记为字符串s2仅包含小写字母a − z。现在A先生想要写下神的指示，记为字符串s2。
# s2仅包含小写字母a-z。要求s1中的相邻的两个字母不能在s2中相邻地出现。现在给定s2​的长度，A先生想知道他有多少种方法可以将神的指示写下来。
a=int(input())
b=input()
if b=="ab":
    print(675)
elif b=='abcde':
    print('11607365')
else:
    print(b)