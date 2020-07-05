import re
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
s.sort()
n = int(input())
if s.count(n):
    print(s.index(n))
elif n > max(s):
    print(len(s))
else:
    index = 0
    for i in s:
        if n < i:
            break
        index += 1
    print(index)