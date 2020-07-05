n=(int)(input())
max=1000010000
cunzai=True
for i in range(n):
    row=[int(n) for n in input().split()]
    row.sort()
    if row[1]<=max:
        max=row[1]
    elif row[0]<=max:
        max=row[0]
    else:
        cunzai=False
        print("NO")
        break
if cunzai:
    print("YES")