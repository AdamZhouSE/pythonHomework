from collections import defaultdict
n = int(input())
no = input().split(" ")
no = [int(i) for i in no]
node = defaultdict(list)
fa = defaultdict(int)
ans = []
for i in range(len(no)):
    node[no[i]] = [0, 0]


def insertnode(r: int, x: int):
    if x == r:
        return
    elif x > r:
        if not node[r][1]:
            node[r][1] = x
            fa[x] = r
            return
        else:
            insertnode(node[r][1], x)
            return
    else:
        if not node[r][0]:
            node[r][0] = x
            fa[x] = r
            return
        else:
            insertnode(node[r][0], x)
            return


for i in range(1, len(no)):
    insertnode(no[0], no[i])
for i in range(len(no)):
    if i == 0:
        ans.append(-1)
    else:
        ans.append(fa[no[i]])
for i in ans:
    print(i)