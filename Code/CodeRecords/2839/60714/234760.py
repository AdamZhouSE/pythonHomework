n = int(input())
temp = dict()
ans = []
for i in range(0, n):
    x = input()
    if x in temp:
        ans.append("YES")
    else:
        temp[x] = True
        ans.append("NO")
for i in ans:
    print(i)
    