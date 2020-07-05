import pandas as pd
n = eval(input())
students = list(map(int, input().split(' ')))
result = dict(pd.value_counts(students))
one, two = result.get(1, 0), result.get(2, 0)
t = min(one, two)
print(t + (one - t) // 3)
