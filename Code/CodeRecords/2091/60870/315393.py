info = input().split()
info = [int(x) for x in info]
edge_list = []
for i in range(info[1]):
    edge = input().split()
    edge = [int(x) for x in edge]
    edge_list.append(edge)
res = info[0] + info[1]
for ch in edge_list:
    res = res + ch[0] + ch[1]
print(res)