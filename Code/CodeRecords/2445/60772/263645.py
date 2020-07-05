import re


def execute(s, t):
    if sorted(s) == sorted(t):
        return 'true'
    else:
        return 'false'


str = input()
li = str.split(',')
s = li[0][5:len(li[0]) - 1]
t = li[1][6:len(li[1]) - 1]
print(execute(s, t))
