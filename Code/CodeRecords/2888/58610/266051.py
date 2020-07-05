import pandas as pd
n, search_time = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))
result = dict(pd.value_counts(arr))
diff = min(result.get(1), result.get(-1)) * 2
for _ in range(search_time):
    search = list(map(int, input().split(' ')))
    t = search[1] - search[0]
    print(1) if t % 2 == 1 and t <= diff else print(0)