n = int(input())
lst = list(map(int, input().split(' ')))
max_ls = []
max_l = 1
for i in range(1, n):
    if lst[i] <= lst[i - 1]:
        max_ls.append(max_l)
        max_l = 0
    max_l += 1
max_ls.append(max_l)
print(max(max_ls))
