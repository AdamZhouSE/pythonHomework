import pandas as pd
s = input()
ini = [dict(pd.value_counts(list(s[i:i + 8]))) for i in range(len(s) - 7)]
count = 0
for _ in range(eval(input())):
    s_dict = dict(pd.value_counts(list(input())))
    for dic in ini:
        if dic == s_dict:
            count += 1
print(count)