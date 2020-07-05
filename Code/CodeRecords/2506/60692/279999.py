list1 = input().split(",")
list1 = [int(i) for i in list1]
i = 0
ans = 1
for i in range(0, len(list1)):
    count = 0
    while list1[i] <= min(list1[i:]):
        if i < len(list1) - 1:
            i = list1.index(min(list1[i + 1:]))
            count += 1
        else:
            count += 1
            break
    if count > ans:
        ans = count
print(ans)