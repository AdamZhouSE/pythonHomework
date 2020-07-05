n, m = [int(x) for x in input().split()]
temp = set([int(x) for x in input().split()])
for i in range(1, n):
    temp = temp.union(set([int(x) for x in input().split()]))
if len(temp) is m:
    print("YES")
else:
    print("NO")
