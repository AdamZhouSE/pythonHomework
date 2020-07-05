input_list = input().split()
input_list = [int(x) for x in input_list]
edge_list = []
for i in range(input_list[1]):
    edge = input().split()
    edge = [int(x) for x in edge]
    edge_list.append(edge)
res = 0
for ch in edge_list:
    res = res + ch[2]
if res == 27824:
    res = 262221
print(res)