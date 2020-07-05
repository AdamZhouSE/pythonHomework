a = eval(input())
l_o = list()
l_w = list()
for i in a:
    if i % 2 == 0:
        l_o.append(i)
    else:
        l_w.append(i)
l_o.sort()
l_w.sort()
l_o.extend(l_w)
print(l_o)

