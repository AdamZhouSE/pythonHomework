list1 = input().split(",")
list1 = [int(i) for i in list1]
i = 0
ans = 1
for i in range(0, len(list1)):
    count = 1
    temp = list1[i]
    for j in range(i + 1, len(list1)):
        if list1[j] >= temp:
            count += 1
            temp = list1[j]
    if count > ans:
        ans = count
print(ans)