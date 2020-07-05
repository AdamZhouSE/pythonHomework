import collections

points=eval(input())
columns = collections.defaultdict(list)
for x, y in points:
    columns[x].append(y)
lastx = {}
ans = float('inf')

for x in sorted(columns):
    column = columns[x]
    column.sort()
    for j, y2 in enumerate(column):
        for i in range(j):
            y1 = column[i]
            if (y1, y2) in lastx:
                ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
            lastx[y1, y2] = x
if ans<float('inf'):
    print(str(ans)+".0000")
else:
    print(0)
# print(ans if ans < float('inf') else 0)