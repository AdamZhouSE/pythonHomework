def cutTree(c: list, b: list, num: int, target: int, res: int, ans: list):
    if num == target:
        ans[0] = max(ans[0], res)
    else:
        cutTree(c, b, num + 1, target, res, ans)
        if c[num - 1] > b[num]:
            c[num - 1] -= b[num]
            cutTree(c, b, num + 1, target, res + 1, ans)
            c[num - 1] += b[num]
        if c[num] > b[num]:
            c[num] -= b[num]
            cutTree(c, b, num + 1, target, res + 1, ans)
            c[num] += b[num]


ans = [0]
road = []
n = eval(input())
a = []
b= []
c = []

for i in range(0, n):
    arr = list(map(int, input().split()))
    a.append(arr[0])
    b.append(arr[1])
    if i != 0:
        c.append(a[-1] - a[-2])

cutTree(c, b, 1, n - 1, 0, ans)
print(ans[0] + 2)
