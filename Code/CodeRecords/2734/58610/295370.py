from pandas import value_counts
n, color, m = list(map(int, input().split(' ')))
flower = list(map(int, input().split(' ')))
for _ in range(m):
    start, end = list(map(int, input().split(' ')))
    t_dict = dict(value_counts(flower[start - 1:end]))
    print(sum([1 for value in t_dict.values() if value > 1]))