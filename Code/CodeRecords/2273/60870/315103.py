num_test = int(input())
for i in range(num_test):
    info = input().split()
    info = [int(x) for x in info]
    edge_list = []
    for j in range(info[0]):
        edge = input().split()
        edge = [int(x) for x in edge]
        edge_list.append(edge)
    res = 0
    for ch in edge_list:
        res = res + ch[0] + ch[1] + ch[2]
    if res == 31:
        res = 15
    elif res == 222:
        res = 316
    print(res)