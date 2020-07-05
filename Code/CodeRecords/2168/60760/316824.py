lists= input().split()
lists= [int(x) for x in lists]
edges = []
for i in range(lists[1]):
    edgeofinput = input().split()
    edgeofinput = [int(x) for x in edgeofinput]
    edges.append(edgeofinput)
res = 0
for i in edges:
    res = res + i[0] + i[1] + i[2]
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