ls = input().split(',')
ls = list(map(int, ls))
res = [-1000] * 3
for num in ls:
    min_num = min(res)
    if num > min_num:
        res[res.index(min_num)] = num
ans = 1
for n in res:
    ans *= n
print(ans)