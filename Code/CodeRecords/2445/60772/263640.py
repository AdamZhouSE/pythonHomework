import re


def execute(s, t):
    if len(s) == len(t) and list(s).sort() == list(t).sort():
        return 'true'
    else:
        return 'false'


str = input()
li = str.split(',')
s = li[0][5:len(li[0]) - 1]
t = li[1][6:len(li[1]) - 1]
print(execute(s, t))
