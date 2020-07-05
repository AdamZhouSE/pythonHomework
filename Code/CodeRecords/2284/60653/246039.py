import re;
m = int(input())
for k in range(0, m):
    ans = []
    tag = []
    n = int(input())
    s = list([int(n) for n in re.findall(r"\-?\d+", input())])
    for i in range(0, n):
        for j in range(i+1, n):
            if s[i] < s[j]:
                ans.append(j-i)
                tag.append(i)
                tag.append(j)
    print(max(ans))