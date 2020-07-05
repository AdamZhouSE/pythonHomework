s = input()
N = len(s)
l = [s[i:] for i in range(N)]
l.sort()
ans = []
for ele in l:
    ans.append(N+1 - len(ele))
print(*ans)

