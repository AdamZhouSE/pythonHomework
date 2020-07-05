from pandas import value_counts
n, q = list(map(int, input().split(' ')))
arr = sorted(map(int, input().split(' ')), reverse=True)
search = []
for _ in range(q):
    a, b = list(map(int, input().split(' ')))
    search += list(range(a, b + 1))
q_dict = dict(value_counts(search))
ques = [item[1] for item in sorted(q_dict.items(), key=lambda x: x[1], reverse=True)]
res = 0
for i in range(len(q_dict)):
    res += ques[i] * arr[i]
print(res)