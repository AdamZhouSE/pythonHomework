from pandas import value_counts
for _ in range(eval(input())):
    n = eval(input())
    nums = list(map(int, input().split(' ')))
    n_dict = sorted(value_counts(nums).items(), key=lambda x: (x[1], -x[0]), reverse=True)
    res = []
    for item in n_dict:
        for i in range(item[1]):
            res.append(item[0])
    print(' '.join([str(i) for i in res]), end=' \n')