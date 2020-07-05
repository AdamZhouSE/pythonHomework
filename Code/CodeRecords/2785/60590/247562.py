times = int(input())
lists = []
for i in range(times):
    n = int(input())
    lists.append(n)

total = sum(lists)
if total % 2 == 0:
    print("YES")
else:
    print("NO")