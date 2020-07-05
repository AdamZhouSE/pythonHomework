cakes = eval(input())
ans = []
if list(reversed(cakes)) == sorted(cakes) or cakes == sorted(cakes):
    ans.append(len(cakes))
else:
    for i in range(len(cakes), 0, -1):
        idx = cakes.index(max(cakes)) + 1
        ans.extend([idx, i])
        tail = cakes[idx:]
        cakes = list(reversed(cakes[:idx]))
        cakes.extend(tail)
        cakes = list(reversed(cakes))[:-1]
print(ans)
