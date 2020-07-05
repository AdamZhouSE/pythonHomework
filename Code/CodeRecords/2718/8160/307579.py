import collections


class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        p = {i: i for i in range(len(s))}

        def f(x):
            if x != p[x]:
                p[x] = f(p[x])
            return p[x]

        for i, j in pairs:
            p[f(j)] = f(i)

        d = collections.defaultdict(list)
        for i, j in enumerate(map(f, p)):
            d[j].append(i)

        ans = list(s)
        for q in d.values():
            t = sorted(ans[i] for i in q)
            for i, c in zip(sorted(q), t):
                ans[i] = c
        return ''.join(ans)


input1 = input()
input2 = input()
temp1 = input2.replace("[", "").replace("]", "").split(",")
group = int(len(temp1) / 2)
mylist = [[0] * 2 for _ in range(group)]
for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        mylist[i][j] = int(temp1[i * 2 + j])
print(Solution().smallestStringWithSwaps(input1, mylist))