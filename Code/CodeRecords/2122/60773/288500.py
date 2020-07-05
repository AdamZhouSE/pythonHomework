x = int(input())
y = int(input())
z = int(input())
flag = 0
l1 = []
l1.append(x)
l1.append(y)
l2 = []
l2.append(x)
l2.append(y)
a = max(x, y) - min(x, y)
l2.append(a)
if x - a > 0 :
    if x-a in l1:
        pass
    else:
        l1.append(x - a)
if y - a > 0 :
    if y-a in l1:
        pass
    else:
        l1.append(y - a)
while (flag == 0):
    len1=len(l1)
    for i in range(2,len(l1),1):
        b=x-l1[i]
        c=y-l1[i]
        if b>0 :
            if b in l2:
                pass
            else:
                l2.append(b)
                d=x-b
                e=y-b
                if d > 0:
                    if d in l1:
                        pass
                    else:
                        l1.append(d)
                if e > 0:
                    if e in l1:
                        pass
                    else:
                        l1.append(e)
        if c>0 :
            if c in l2:
                pass
            else:
                l2.append(c)
                d = x - c
                e = y - c
                if d > 0:
                    if d in l1:
                        pass
                    else:
                        l1.append(d)
                if e > 0:
                    if e in l1:
                        pass
                    else:
                        l1.append(e)
    if len(l1)==len1:
        break
if z in l2:
    print(True)
else:
    print(False)
