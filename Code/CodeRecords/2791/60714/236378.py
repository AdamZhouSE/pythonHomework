n = int(input())
temp = [int(x) for x in input().split()]
ans = []
a = 1
i = 0
temp.append(0)
while i <= n:
    if i is n:
        ans.append(a - 1)
        break
    if temp[i] is a:
        a += 1
        i += 1
    elif temp[i] is not a:
        ans.append(a - 1)
        a = 1
print(len(ans))
for i in range(0, len(ans) - 1):
    print(ans[i], end=" ")
print(ans[len(ans) - 1])

