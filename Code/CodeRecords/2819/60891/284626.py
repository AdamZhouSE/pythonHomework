n = int(input())
list_s = [int(i) for i in input().split()]
list_1 = []
list_2 = []
list_3 = []
ans = 0
for i in list_s:
    if i == 4:
        ans += 1
    elif i == 3:
        list_3.append(i)
    elif i == 2:
        list_2.append(i)
    else:
        list_1.append(1)
ans += len(list_3)
for i in range(len(list_3)):
    if len(list_1) > 0:
        list_1.pop()
if len(list_2) % 2 == 1:
    ans += (len(list_2) // 2)
    ans += 1
    for i in range(2):
        if len(list_1) > 0:
            list_1.pop()
    if len(list_1) % 4 == 0:
        ans += (len(list_1) // 4)
    else:
        ans += (len(list_1) // 4)
        ans += 1
else:
    ans += (len(list_2) // 2)
    if len(list_1) % 4 == 0:
        ans += (len(list_1) // 4)
    else:
        ans += (len(list_1) // 4)
        ans += 1
print(ans)