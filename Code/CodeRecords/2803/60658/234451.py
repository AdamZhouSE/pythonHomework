n,m=[int(x) for x in input().split()]
ans = set()
for i in range(n):
    temp = input().split()
    li = temp[1:]
    for i in li:
        ans.add(i)
print("YES" if len(ans)==m else "NO")