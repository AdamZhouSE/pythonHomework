import itertools

answers = list(map(int, input().split(',')))
ans = 0
for key, group in itertools.groupby(answers):
    group = list(group)
    item = divmod(len(group), key + 1)
    ans += item[0] * (key + 1) + ((key + 1) if item[1] else 0)
print(ans)
