info = input().split()
info = [int(x) for x in info]
edge_list = []
for i in range(info[1]):
    edge = input().split()
    edge_list.append(edge)
res = 0
for ch in edge_list:
    res = res + ch[0] + ch[1] + ch[2]
print(res)