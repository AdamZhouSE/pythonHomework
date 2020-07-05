n = int(input())
k = int(input())

lst = []
for i in range(1, n + 1):
    lst.append(i)
ans = ''
i = n
while i > 1:
    temp = 1
    for j in range(1, i):
        temp = temp * j
    target = lst[k // temp]
    del lst[k // temp]
    ans = ans + str(target)
    k = k % temp
    if k == 1:
        break
    i -= 1

for x in lst:
    ans += str(x)

print(ans)
