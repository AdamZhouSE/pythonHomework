n = int(input())
list_loc = [int(i) for i in input().split()]
count_1 = 0
count_2 = 0
for i in list_loc:
    if i % 2 == 1:
        count_1 += 1
    else:
        count_2 += 1
ans = min(count_2, count_1)
print(ans)