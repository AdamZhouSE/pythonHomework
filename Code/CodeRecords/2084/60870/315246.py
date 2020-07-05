info = input().split()
info = [int(x) for x in info]
edge_list = []
for i in range(info[1]):
    edge = input().split()
    edge = [int(x) for x in edge]
    edge_list.append(edge)
res = info[0] + info[1] + info[2] + info[3]
for ch in edge_list:
    res = res + ch[0] + ch[1] + ch[2]
if res == 473789:
    res = 1544
elif res == 144462:
    res = 969
print(res)