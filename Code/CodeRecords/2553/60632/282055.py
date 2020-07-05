def in_order(x: list):
    res = [0]
    for i in x:
        this, lc, rc = i[0], i[1], i[2]
        index = res.index(this)
        if lc != -1:
            res.insert(index, lc)
        if rc != -1:
            res.insert(index + 2, rc)
    return res


def judge(x: list) -> bool:  # 判断该序列是否是非下降序列
    for i in range(1, len(x)):
        if x[i] < x[i-1]:
            return False
    return True


n = int(input())
node = list(map(int, input().split(' ')))
# link存放二叉树的连接情况，分别为 本节点、左子节点、右子节点 的节点号
link = [[i, -1, -1] for i in range(n)]
for i in range(1, n):
    fa, t = map(int, input().split(' '))
    if t == 0:
        link[fa - 1][1] = i
    else:
        link[fa - 1][2] = i
# for i in link:
#     print(i)
inord = in_order(link)
for i in range(len(inord)):
    inord[i] = node[inord[i]]
# print(inord)
num = int(pow(2, n)) - 1
ans = 0
for i in range(num, 0, -1):
    sup = list(bin(i)[2:])
    while len(sup) != n:
        sup.insert(0, '0')
    tmp = []
    for j in range(len(sup)):
        if sup[j] == '1':
            tmp.append(inord[j])
    if judge(tmp):
        ans = max(ans, len(tmp))
print(n-ans)
