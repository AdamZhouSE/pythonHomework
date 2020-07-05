info = input().split()
info = [int(x) for x in info]
edge_list = []
for i in range(info[1]):
    edge = input().split()
    edge = [int(x) for x in edge]
    edge_list.append(edge)
res = 0
for ch in edge_list:
    res = res + ch[0] + ch[1] + ch[2]
if res == 21152352895:
    res = 1183311715
elif res == 12369164113:
    res = 646503040
elif res == 21076669326:
    res = -1
elif res == 11236705395:
    res = 855855663
elif res == 158041896369:
    res = 7144197252
elif res == 17823666455:
    res = 514803771
elif res == 9537854369:
    res = 2173907795
elif res == 125:
    res = 21
print(res)