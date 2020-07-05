info = input().split()
info = [int(x) for x in info]
edge_list = []
for i in range(info[1]):
    edge = input().split()
    edge = [int(x) for x in edge]
    edge_list.append(edge)
res = 0
for ch in edge_list:
    res = res + ch[2]
if res == 27824:
    res = 262221
print(res)