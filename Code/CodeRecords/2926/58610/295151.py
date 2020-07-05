from pandas import value_counts
n = eval(input())
coins = list(map(int, input().split(' ')))
n_dict = dict(value_counts(coins))
print(max([value for value in n_dict.values()]))