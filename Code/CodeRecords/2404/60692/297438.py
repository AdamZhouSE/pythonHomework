from collections import defaultdict
treenode = defaultdict(list)
l1 = input().split(" ")
n, s = int(l1[0]), int(l1[1])
list1 = input().split(" ")
list1 = [int(i) for i in list1]
list1.insert(0, 0)
ans = []
count = []
for i in range(n - 1):
    node = input().split(" ")
    treenode[int(node[0])].append(int(node[1]))


def dfs(dic: defaultdict, root: int, cnt: int):
    cnt += list1[root]
    if cnt == s:
        count.append(1)
        return
    if not dic[root]:
        return
    if len(dic[root]) == 1:
        dfs(dic, dic[root][0], cnt)
    else:
        dfs(dic, dic[root][0], cnt)
        dfs(dic, dic[root][1], cnt)


for i in range(1, n + 1):
    dfs(treenode, i, 0)
print(sum(count))