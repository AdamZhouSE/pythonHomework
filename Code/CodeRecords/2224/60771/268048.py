#17
s = input()
l = list(s)
# print(max(l))
for i in range(0,len(l)-1):
    Max = max(l)
    if Max == s[i]:
        l.remove(Max)
        continue
    else:
        Min = min(l)
        i1 = s.index(Max)
        i2 = s.index(Min)
        sList = list(s)
        sList[i1] = Min
        sList[i2] = Max
        s = "".join(sList)
        break
print(s)