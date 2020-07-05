citations = input().split(',')

for i in range(len(citations)):
    citations[i] = int(citations[i])

flag = False
ans = 0

for index, c in enumerate(citations):
    if c >= len(citations) - index:
        flag = True
        ans = c
        break

if flag:
    print(ans)
else:
    print(0)