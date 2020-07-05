import re


def execute(s, t):
    return sorted(s) == sorted(t)


str = input()
li = str.split(',')
s = li[0][5:len(li[0]) - 1]
t = li[1][6:len(li[1]) - 1]
print(execute(s, t))
