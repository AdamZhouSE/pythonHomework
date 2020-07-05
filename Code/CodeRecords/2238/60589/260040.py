import collections

answers = eval(input())
cnt = dict(collections.Counter(answers))
res = 0
for i in cnt:
    res+=cnt[i]+(-cnt[i]%(int(i)+1))
print(res)