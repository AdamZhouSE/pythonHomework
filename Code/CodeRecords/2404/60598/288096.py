class Tree:
    val = 0

    def __init__(self, x):
        self.son = []
        self.val = x


line1 = input().split(" ")
N = int(line1[0])
S = int(line1[1])
nums = list(map(int, input().split(" ")))
Trees = [Tree(i) for i in range(len(nums))]
for i in range(len(nums)):
    Trees[i].val = nums[i]
for j in range(N - 1):
    temp = input().split(" ")
    f = int(temp[0]) - 1
    s = int(temp[1]) - 1
    Trees[f].son.append(s)


def dfs(root, x):
    result = 0
    if root.val + x == S:
        result += 1
    for s in root.son:
        result += dfs(Trees[s], root.val + x)
    return result


ans = 0
for k in range(len(Trees)):
    ans += dfs(Trees[k], 0)
print(ans)
#
