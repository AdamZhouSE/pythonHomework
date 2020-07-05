# 题目描述
# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 输入描述
# 一个二叉树
# 输出描述
# 二叉树的最小深度。最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
tree = []

x = input().strip()
x = x[1:len(x)-1]
for i in x.split(","):
    if i == "null":
        tree.append(None)
    else:
        tree.append(int(i))
cnt = 0
for idx in range(len(tree)):
    if tree[idx] is None:
        cnt = idx
        break
num = 0
level = 0

while True:
    num += pow(2, level)
    if num >= cnt:
        break

print(num-1)