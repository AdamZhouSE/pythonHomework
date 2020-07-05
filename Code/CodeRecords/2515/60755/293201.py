def solve(s, l):
    res = []
    fro = 0
    for i in range(len(s)):
        if s[i] == "1":
            res.append(sum(l[fro:i + 1]))
            fro = i + 1
    res.append(sum(l[fro:]))
    return max(res)


def judge(s, k):
    res = 0
    for i in s:
        if i == "1":
            res = res + 1
    return res == k


all = input().split(",")
num = int(input())
for i in range(len(all)):
    all[i] = int(all[i])
res = []
for i in range(pow(2, len(all) - 1)):
    temp = bin(i)[2:]
    while len(temp) != len(all) - 1:
        temp = "0" + temp
    if judge(temp, num-1):
        res.append(solve(temp, all))
print(min(res))