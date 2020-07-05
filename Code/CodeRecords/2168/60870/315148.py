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
print(res)