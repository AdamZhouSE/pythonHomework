n = int(input())
a = [int(i) for i in input().split()]
list_change = []
for i in range(n - 1):
    if a[i] != a[i + 1]:
        list_change.append(i)
list_len = []
for i in list_change:
    left_be = i
    right_be = i + 1
    l = 2
    while left_be >= 1 and right_be <= n - 2 and a[left_be] == a[left_be - 1] and a[right_be] == a[right_be + 1]:
        l += 2
        left_be -= 1
        right_be += 1
    list_len.append(l)
print(max(list_len))
