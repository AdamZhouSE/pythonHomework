import re


t = int(input())
while t:
    s = input()
    s = re.sub('[^a-zA-Z]','',s)
    s = s.lower()
    a = list(s)
    b = list(s)
    b.reverse()
    if a == b:
        print('YES')
    else:
        print('NO')
    t -= 1
    