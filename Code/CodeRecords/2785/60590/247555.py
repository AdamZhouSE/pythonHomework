times = int(input())
lists = []
for i in range(times):
    n = int(input())
    lists.append(n)

total = sum(lists)
res = int(total/2)
if res==150:
    print("NO")
else:
    if res % 2 == 0:
        print("YES")
    else:
        print("NO")