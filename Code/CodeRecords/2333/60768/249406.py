import math

x = int(input())
y = int(input())
bound = int(input())
re = []
for p in range(int(math.log(bound, x+0.1)+1)):
    for q in range(int(math.log(bound, y+0.1)+1)):
        re.append(pow(x, p) + pow(y, q))
ans = []
for e in re:
    if e not in ans and e <= bound:
        ans.append(e)
ans.sort()
print(ans)