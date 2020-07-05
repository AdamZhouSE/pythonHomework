
from collections import Counter


def minutes(a, result):
    minutes = []
    e = [i for i in a if i <= 5]
    minutes.append(max(e))
    a.remove(max(e))
    minutes.append(a[0])
    lists = result + [':'] + minutes
    li1 = [str(y) for y in lists]
    li2 = ''.join(li1)
    print(li2)


    
result = []
info = input().split(',')
a = [int(y) for y in info]
c = Counter(a)
if c.get(2) != None:
    if c.get(3) != None or c.get(2) > 1 or c.get(1) != None or c.get(0) != None:
        result.append(2)
        a.remove(2)
        c1 = [i for i in a if i <= 3]
        result.append(max(c1))
        a.remove(max(c1))
        minutes(a, result)
    else:
        print("")
elif c.get(0) != None or c.get(1) != None:
    d = [i for i in a if i <= 1]
    result.append(max(d))
    a.remove(max(d))
    result.append(max(a))
    a.remove(max(a))
    minutes(a, result)
else:
    print("")