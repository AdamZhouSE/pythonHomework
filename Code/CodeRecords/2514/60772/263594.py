import re


def execute(s, t):
    if s == '':
        return True
    index = -1
    for i in s:
        index = t.find(i, index + 1)
        if index == -1:
            return False
    return True


s = input()
t = input()
print(execute(s, t))
