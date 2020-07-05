class Tree:
    val = 0
    left = None
    right = None
    weight = 0

    def __init__(self, x):
        self.val = x


line1 = input().split(" ")
num = int(line1[0])
root = Tree(line1[1])
store = dict()
store[int(line1[1])] = root
for i in range(num):
    temp = list(map(int, input().split(" ")))
    if not temp[0] in store:
        node = Tree(temp[0])
        store[temp[0]] = node
    if temp[1] != 0 and not temp[1] in store:
        node = Tree(temp[1])
        store[temp[1]] = node
    if temp[2] != 0 and not temp[2] in store:
        node = Tree(temp[2])
        store[temp[2]] = node
    f = store[temp[0]]
    f.weight = temp[3]
    if temp[1] in store:
        f.left = store[temp[1]]
    if temp[2] in store:
        f.right = store[temp[2]]
target = int(input())
Max = 0


def dfs(root, sum, level):
    if root is None:
        return 0
    count = 0
    if sum + root.weight == target:
        count = level + 1
    return max(count, dfs(root.right,sum+root.weight,level+1), dfs(root.left, sum + root.weight, level+1))


for k in store:
    Max = max(Max, dfs(store[k], 0, 0))
print(Max)
