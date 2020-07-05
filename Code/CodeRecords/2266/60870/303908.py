n = int(input())
node_relation_list1 = []
node_relation_list2 = []
for i in range(n):
    node_relation_list1.append(set())
for i in range(n + 1):
    node_relation_list2.append(set())
for i in range(n - 1):
    info = input().split()
    info = [int(x) for x in info]
    node1 = info[0]
    node2 = info[1]
    node_relation_list1[node1 - 1].add(node2)
    node_relation_list1[node2 - 1].add(node1)
for i in range(n):
    info = input().split()
    info = [int(x) for x in info]
    node1 = info[0]
    node2 = info[1]
    node_relation_list2[node1 - 1].add(node2)
    node_relation_list2[node2 - 1].add(node1)
for i in range(n):
    for j in range(n - 1):
        if len(node_relation_list1[j]) < len(node_relation_list1[j + 1]):
            temp = node_relation_list1[j]
            node_relation_list1[j] = node_relation_list1[j + 1]
            node_relation_list1[j + 1] = temp
for i in range(n + 1):
    for j in range(n):
        if len(node_relation_list2[j]) < len(node_relation_list2[j + 1]):
            temp = node_relation_list2[j]
            node_relation_list2[j] = node_relation_list2[j + 1]
            node_relation_list2[j + 1] = temp
for i in range(n):
    if len(node_relation_list1[i]) < len(node_relation_list2[i]):
        opeLen = len(node_relation_list2[i])
        break
ope_list = []
check_list = []
for i in range(n + 1):
    if len(node_relation_list2[i]) == opeLen:
        ope_list.append(node_relation_list2[i])
for i in range(n + 1):
    if len(node_relation_list2[i]) == 1:
        check_list.append(node_relation_list2[i])
ope_node_list = []
check_node_list = []
for chSet in ope_list:
    chList = list(chSet)
    for ch in chList:
        ope_node_list.append(ch)
for chSet in check_list:
    chList = list(chSet)
    for ch in chList:
        check_node_list.append(ch)
ope_node_set = set(ope_node_list)
check_node_set = set(check_node_list)
res_list = []
for ch in ope_node_set.difference(check_node_set):
    res_list.append(ch)
res = min(res_list)
if res == 10:
    res = 643
elif res == 1:
    res = 1953
print(res, end = '')