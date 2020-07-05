from collections import defaultdict
count = defaultdict(int)
names = []
n = int(input())
ans = []
for i in range(n):
    name = input()
    count[name] = 0
    names.append(name)
m = int(input())
for i in range(m):
    n = input()
    if not names.count(n):
        ans.append("WRONG")
    else:
        if count[n] >= 1:
            ans.append("REPEAT")
        else:
            ans.append("OK")
            count[n] += 1
for i in ans:
    print(i)