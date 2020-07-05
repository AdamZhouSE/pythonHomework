m, n = map(int, input().split())
first = []
mother = []
res = []
name = []
for i in range(0, m):
    s = input().split()
    first.append(s[0])
    mother.append(int(s[1]))
for i in range(0, m):
    temp = first[i]
    j = mother[i]
    while j > 0:
        j -= 1
        if mother.count(j) > 0 or mother[j] > 0:
            temp += first[j]
            j = mother[j]
    name.append(temp)

for i in range(0, n):
    ans = 0
    want = input()
    q = len(want)
    for j in range(0, m):
        if want == name[j][0:q]:
            ans += 1
    res.append(ans)
for i in range(0, n):
    print(res[i])