import re;
a = int(input())
ans = []
for i in range(0, a):
    m = int(input())
    s = list([int(n) for n in re.findall(r"\d+", input())])
    mul = 1
    for j in s:
        mul *= j
    for k in range(0, m):
        ans.append(int(mul/s[k]))
    ans.append("end")

for i in ans:
    if i == "end":
        print("")
    else:
        print('%d' % i, end=' ')