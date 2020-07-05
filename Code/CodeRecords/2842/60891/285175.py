n = int(input())
p = [-99]
for i in range(n):
    p.append(int(input()))
list_count = []
for i in range(1, n + 1):
    count = 1
    if p[i] != -1:
        manager = i
        sup = p[manager]
        while sup != -1:
            count += 1
            manager = sup
            sup = p[manager]
    list_count.append(count)
print(max(list_count))